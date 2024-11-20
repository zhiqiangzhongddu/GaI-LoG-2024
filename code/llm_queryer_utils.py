import sys
import os
from pathlib import PurePath
import json
from tqdm import tqdm
import time
import tiktoken
from transformers import LlavaNextProcessor, LlavaNextForConditionalGeneration
import torch
from PIL import Image
import requests

from openai import OpenAI
from openai_env import OPENAI_API_KEY

from code.utils import init_path, project_root_path


def num_tokens_from_messages(
        messages,
        model,
):
    """Return the number of tokens used by a list of messages."""
    try:
        enc = tiktoken.encoding_for_model(model)
    except KeyError:
        print("Warning: model not found. Using cl100k_base encoding.")
        enc = tiktoken.get_encoding("cl100k_base")

    total_tokens = 0
    for message in messages:
        content = message['content']
        if isinstance(content, str):
            tokens = enc.encode(content)
            total_tokens += len(tokens)
        elif isinstance(content, list):
            for item in content:
                if 'text' in item:
                    tokens = enc.encode(item['text'])
                    total_tokens += len(tokens)
                if 'image_url' in item:
                    # Assuming URLs are not tokenized, otherwise adjust accordingly
                    tokens = enc.encode(item['image_url']['url'])
                    total_tokens += len(tokens)
    return total_tokens


def extract_urls(messages):
    urls = []
    for message in messages:
        for content in message.get('content', []):
            if isinstance(content, dict) and content.get('type') == 'image_url':
                urls.append(content['image_url']['url'])
    return urls


def get_image_size(url):
    try:
        # Fetch the image from the URL
        response = requests.get(url)
        response.raise_for_status()

        # Get image size in bytes
        image_size_bytes = len(response.content)

        return image_size_bytes

    except requests.RequestException as e:
        return f"Error fetching image: {e}"
    except Exception as e:
        return f"Error processing image: {e}"


def img_sizes_from_messages(
        messages,
        use_image,
):
    """Return the size of images used by a list of messages."""

    if use_image is False:
        return 0

    elif use_image is True:
        img_size = 0
        urls = extract_urls(messages)
        for url in urls:
            img_size += get_image_size(url)
        return img_size


def get_openai_limit():
    # RPM limit (adjust according to your plan)
    rpm_limit = 5000
    # TPM limit (adjust according to your plan)
    tpm_limit = 40000
    # Context window size
    cws_limit = 200000
    # Image size
    # img_limit = 2e+7
    # img_limit = 1.5e+7
    img_limit = 1.e+7

    return rpm_limit, tpm_limit, cws_limit, img_limit


def query_openai_batch(
        client,
        llm_model,
        task_type,
        algorithm,
        num_graphs,
        text_encoder,
        task_name,
        cot,
        bag,
        use_text,
        use_image,
        k,
        seed,
        demo_test,
        batch_message_list,
        batch_start_id,
        rpm_limit,
):

    batch_response_list = []

    for send_id, message in enumerate(batch_message_list):
        flag = check_responses(
            llm_model,
            task_type,
            algorithm,
            num_graphs,
            text_encoder,
            task_name,
            cot,
            bag,
            use_text,
            use_image,
            k,
            seed,
            demo_test,
            cache=True,
            sample_id=batch_start_id + send_id
        )
        if flag:
            response = load_responses(
                task_type=task_type,
                algorithm=algorithm,
                num_graphs=num_graphs,
                text_encoder=text_encoder,
                task_name=task_name,
                cot=cot,
                bag=bag,
                use_text=use_text,
                use_image=use_image,
                k=k,
                llm_model=llm_model,
                seed=seed,
                demo_test=demo_test,
                cache=True,
                sample_id=batch_start_id + send_id,
            )
            batch_response_list.append(response)
        else:
            chat_completion = client.chat.completions.create(
                model=llm_model,
                messages=message,
            )
            response = chat_completion.choices[0].message.content
            batch_response_list.append(response)

            # Save response of each request, in case any errors stop the execution
            save_responses(
                responses=response,
                llm_model=llm_model,
                task_type=task_type,
                algorithm=algorithm,
                num_graphs=num_graphs,
                text_encoder=text_encoder,
                task_name=task_name,
                cot=cot,
                bag=bag,
                use_text=use_text,
                use_image=use_image,
                k=k,
                seed=seed,
                demo_test=demo_test,
                cache=True,
                sample_id=batch_start_id + send_id,
            )

            # Rate limiting to stay within RPM limit
            time.sleep(60 / rpm_limit)

    return batch_response_list



def query_openai(
        llm_model,
        message_list,
        task_type,
        algorithm,
        num_graphs,
        text_encoder,
        task_name,
        cot,
        bag,
        use_text,
        use_image,
        k,
        seed,
        demo_test,
):
    assert llm_model in ["gpt-4o", "gpt-4-turbo"], f"Invalid LLM option: {llm_model}."

    rpm_limit, tpm_limit, cws_limit, img_limit = get_openai_limit()

    # Set up OpenAI API
    client = OpenAI(
        api_key=OPENAI_API_KEY,
    )

    # Save all queries
    response_list = []

    # Run batch queries
    batch_message_list = []
    batch_message_token_num = 0
    batch_message_img_size = 0
    batch_start_id = 0
    display = "Querying LLM"
    for message_id, message in enumerate(tqdm(message_list, desc=display)):

        num_tokens = num_tokens_from_messages(
            messages=message,
            model=llm_model
        )
        if num_tokens > tpm_limit:
            sys.exit(f"Message token number is large than limit {tpm_limit}.")
        if num_tokens >= cws_limit:
            sys.exit(
                f"Message context length is {num_tokens}, "
                f"larger than Context Window Size limit {cws_limit}."
            )
        batch_message_token_num += num_tokens

        img_sizes = img_sizes_from_messages(
            messages=message,
            use_image=use_image,
        )
        if img_sizes > img_limit:
            sys.exit(f"Message image size is large than limit {img_limit}.")
        batch_message_img_size += img_sizes

        if (((batch_message_token_num >= tpm_limit) or (batch_message_img_size >= img_limit))
                and (message_id < len(message_list) - 1)):

            batch_response_list = query_openai_batch(
                client=client,
                llm_model=llm_model,
                task_type=task_type,
                algorithm=algorithm,
                num_graphs=num_graphs,
                text_encoder=text_encoder,
                task_name=task_name,
                cot=cot,
                bag=bag,
                use_text=use_text,
                use_image=use_image,
                k=k,
                seed=seed,
                demo_test=demo_test,
                batch_message_list=batch_message_list,
                batch_start_id=batch_start_id,
                rpm_limit=rpm_limit,
            )
            response_list += batch_response_list
            batch_message_list = [message]
            batch_start_id = message_id

        elif message_id == len(message_list) - 1:
            batch_message_list.append(message)

            batch_response_list = query_openai_batch(
                client=client,
                llm_model=llm_model,
                task_type=task_type,
                algorithm=algorithm,
                num_graphs=num_graphs,
                text_encoder=text_encoder,
                task_name=task_name,
                cot=cot,
                bag=bag,
                use_text=use_text,
                use_image=use_image,
                k=k,
                seed=seed,
                demo_test=demo_test,
                batch_message_list=batch_message_list,
                batch_start_id=batch_start_id,
                rpm_limit=rpm_limit,
            )
            response_list += batch_response_list

        else:
            batch_message_list.append(message)

    return response_list


def query_llava(
        llm_model,
        message_list,
        task_type,
        algorithm,
        num_graphs,
        text_encoder,
        task_name,
        cot,
        bag,
        use_text,
        use_image,
        k,
        seed,
        demo_test,
        gpu_id,
):
    assert llm_model in ["llava-v1.6-mistral-7b-hf"], f"Invalid LLM option: {llm_model}."
    gpu = "cuda:{}".format(gpu_id)

    # setup LLM
    processor = LlavaNextProcessor.from_pretrained(
        "llava-hf/llava-v1.6-mistral-7b-hf"
    )

    model = LlavaNextForConditionalGeneration.from_pretrained(
        "llava-hf/llava-v1.6-mistral-7b-hf",
        torch_dtype=torch.float16,
        low_cpu_mem_usage=True
    )
    model.to(gpu)

    # Save all queries
    response_list = []

    # Run queries
    display = "Querying LLM"
    for message_id, message in enumerate(tqdm(message_list, desc=display)):
    # for message_id, message in enumerate(tqdm(message_list[:1], desc=display)):
        flag = check_responses(
            llm_model,
            task_type,
            algorithm,
            num_graphs,
            text_encoder,
            task_name,
            cot,
            bag,
            use_text,
            use_image,
            k,
            seed,
            demo_test,
            cache=True,
            sample_id=message_id,
        )
        if flag:
            response = load_responses(
                task_type=task_type,
                algorithm=algorithm,
                num_graphs=num_graphs,
                text_encoder=text_encoder,
                task_name=task_name,
                cot=cot,
                bag=bag,
                use_text=use_text,
                use_image=use_image,
                k=k,
                llm_model=llm_model,
                seed=seed,
                demo_test=demo_test,
                cache=True,
                sample_id=message_id,
            )
        else:
            conversation = [message[0]]
            _image_url = message[-1]["image_url"]
            # print(0, _image_url)
            image = Image.open(requests.get(_image_url, stream=True).raw)

            prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)
            inputs = processor(image, prompt, return_tensors="pt").to(gpu)

            # autoregressively complete prompt
            output = model.generate(
                **inputs, max_new_tokens=100, pad_token_id=None, eos_token_id=None
            )
            response = processor.decode(output[0], skip_special_tokens=True)

            # Save response of each request, in case any errors stop the execution
            save_responses(
                responses=response,
                llm_model=llm_model,
                task_type=task_type,
                algorithm=algorithm,
                num_graphs=num_graphs,
                text_encoder=text_encoder,
                task_name=task_name,
                cot=cot,
                bag=bag,
                use_text=use_text,
                use_image=use_image,
                k=k,
                seed=seed,
                demo_test=demo_test,
                cache=True,
                sample_id=message_id,
            )

        response_list.append(response)

    return response_list


def query_llm(
        llm_model,
        message_list,
        task_type,
        algorithm,
        num_graphs,
        text_encoder,
        task_name,
        cot,
        bag,
        use_text,
        use_image,
        k,
        seed,
        demo_test,
        gpu_id,
):
    if llm_model in ["gpt-4o", "gpt-4-turbo"]:
        response_list = query_openai(
            llm_model=llm_model,
            message_list=message_list,
            task_type=task_type,
            algorithm=algorithm,
            num_graphs=num_graphs,
            text_encoder=text_encoder,
            task_name=task_name,
            cot=cot,
            bag=bag,
            use_text=use_text,
            use_image=use_image,
            k=k,
            seed=seed,
            demo_test=demo_test,
        )
    elif llm_model in ["llava-v1.6-mistral-7b-hf"]:
        response_list = query_llava(
            llm_model=llm_model,
            message_list=message_list,
            task_type=task_type,
            algorithm=algorithm,
            num_graphs=num_graphs,
            text_encoder=text_encoder,
            task_name=task_name,
            cot=cot,
            bag=bag,
            use_text=use_text,
            use_image=use_image,
            k=k,
            seed=seed,
            demo_test=demo_test,
            gpu_id=gpu_id,
        )
    else:
        raise ValueError("Invalid LLM option.")
    
    return dict(zip(range(len(response_list)), response_list))


def get_file_path(
        llm_model,
        provider,
        task_type,
        algorithm,
        num_graphs,
        text_encoder,
        task_name,
        cot,
        bag,
        use_text,
        use_image,
        seed,
        demo_test,
        cache=False,
        sample_id=0,
):
    if demo_test:
        folder = "demo_generated_responses"
        cache_folder = "demo_cache_responses"
    else:
        folder = "generated_responses"
        cache_folder = "cache_responses"

    file_path = PurePath(
        project_root_path,
        "output",
        folder,
        provider + "-" + llm_model,
        algorithm,
        text_encoder,
        # "task-{}-algo-{}-num_graphs-{}-text_encoder-{}-task-{}-cot-{}-bag-{}-text-{}-image-{}-seed-{}.json".format(
        "{}-{}-{}-{}-{}-{}-{}-{}-{}.json".format(
            task_type,
            algorithm,
            num_graphs,
            text_encoder,
            task_name,
            str(cot),
            str(bag),
            str(use_text),
            str(use_image),
            seed,
        ),
    ) if not cache else PurePath(
        project_root_path,
        "output",
        cache_folder,
        provider + "-" + llm_model,
        algorithm,
        text_encoder,
        # "task-{}-algo-{}-num_graphs-{}-text_encoder-{}-task-{}-cot-{}-bag-{}-text-{}-image-{}-seed-{}-sample_id-{}.json".format(
        "{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}.json".format(
            task_type,
            algorithm,
            num_graphs,
            text_encoder,
            task_name,
            str(cot),
            str(bag),
            str(use_text),
            str(use_image),
            seed,
            sample_id,
        ),
    )

    return file_path


def check_responses(
        llm_model,
        task_type,
        algorithm,
        num_graphs,
        text_encoder,
        task_name,
        cot,
        bag,
        use_text,
        use_image,
        k,
        seed,
        demo_test,
        cache=False,
        sample_id=0,
):
    if llm_model in ["gpt-4o", "gpt-4-turbo"]:
        provider = "openai"
    elif llm_model in ["llava-v1.6-mistral-7b-hf"]:
        provider = "llava"
    else:
        raise ValueError("Invalid LLM option.")

    task_type = task_type + f"_{k}" if task_type == "few_shot" else task_type

    file_path = get_file_path(
        llm_model=llm_model,
        provider=provider,
        task_type=task_type,
        algorithm=algorithm,
        num_graphs=num_graphs,
        text_encoder=text_encoder,
        task_name=task_name,
        cot=cot,
        bag=bag,
        use_text=use_text,
        use_image=use_image,
        seed=seed,
        demo_test=demo_test,
        cache=cache,
        sample_id=sample_id,
    )

    if os.path.isfile(file_path):
        # print(f"{file_path} has generated responses")
        return True
    else:
        return False


def save_responses(
        responses,
        llm_model,
        task_type,
        algorithm,
        num_graphs,
        text_encoder,
        task_name,
        cot,
        bag,
        use_text,
        use_image,
        k,
        seed,
        demo_test,
        cache=False,
        sample_id=0,
):
    if llm_model in ["gpt-4o", "gpt-4-turbo"]:
        provider = "openai"
    elif llm_model in ["llava-v1.6-mistral-7b-hf"]:
        provider = "llava"
    else:
        raise ValueError("Invalid LLM option.")

    task_type = task_type + f"_{k}" if task_type == "few_shot" else task_type

    file_path = get_file_path(
        llm_model=llm_model,
        provider=provider,
        task_type=task_type,
        algorithm=algorithm,
        num_graphs=num_graphs,
        text_encoder=text_encoder,
        task_name=task_name,
        cot=cot,
        bag=bag,
        use_text=use_text,
        use_image=use_image,
        seed=seed,
        demo_test=demo_test,
        cache=cache,
        sample_id=sample_id,
    )

    init_path(dir_or_file=file_path)
    with open(file_path, 'w') as file:
        json.dump(responses, file, indent=2)


def load_responses(
        task_type,
        algorithm,
        num_graphs,
        text_encoder,
        task_name,
        cot,
        bag,
        use_text,
        use_image,
        k,
        llm_model,
        seed,
        demo_test,
        cache=False,
        sample_id=0,
):
    if llm_model in ["gpt-4o", "gpt-4-turbo"]:
        provider = "openai"
    elif llm_model in ["llava-v1.6-mistral-7b-hf"]:
        provider = "llava"
    else:
        raise ValueError("Invalid LLM option.")

    task_type = task_type + f"_{k}" if task_type == "few_shot" else task_type

    file_path = get_file_path(
        llm_model=llm_model,
        provider=provider,
        task_type=task_type,
        algorithm=algorithm,
        num_graphs=num_graphs,
        text_encoder=text_encoder,
        task_name=task_name,
        cot=cot,
        bag=bag,
        use_text=use_text,
        use_image=use_image,
        seed=seed,
        demo_test=demo_test,
        cache=cache,
        sample_id=sample_id,
    )

    with open(file_path, 'r') as file:
        responses = json.load(file)

    return responses
