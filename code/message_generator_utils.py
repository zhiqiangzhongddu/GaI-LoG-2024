import os
from pathlib import PurePath
import json
import copy

from code.utils import init_path, project_root_path
from code.message_dictionaries import system_instruction, format_postfix, openai_message_template, llava_message_template
from code.image_generator_utils import get_image_links


def zero_shot_openai(
        examples,
        algorithm,
        task,
        num_graphs,
        use_text,
        use_image,
        seed,
):
    instruction = system_instruction
    image_links = get_image_links(
        algorithm=algorithm,
        num_graphs=num_graphs,
        seed=seed,
    )
    postfix = format_postfix[task]

    messages = {}

    for key, example in examples.items():
        if use_text is True and use_image is False:
            _template = copy.deepcopy(
                openai_message_template["zero_shot_text"]
            )
            _template["content"] = example["question"] + postfix

        elif use_text is False and use_image is True:
            _template = copy.deepcopy(
                openai_message_template["zero_shot_image"]
            )
            _template["content"][0]["text"] = _template["content"][0]["text"].format(
                "\nQ:" + example["question"].split("\nQ:")[1]
            ) + postfix
            _template["content"][1]["image_url"]["url"] = image_links[int(key)]

        elif use_text is True and use_image is True:
            _template = copy.deepcopy(
                openai_message_template["zero_shot_text_image"]
            )
            _template["content"][0]["text"] = _template["content"][0]["text"].format(
                example["question"]
            ) + postfix
            _template["content"][1]["image_url"]["url"] = image_links[int(key)]

        else:
            raise ValueError("Invalid message option.")

        messages[key] = [
            instruction,
            _template
        ]
    
    return messages


def zero_shot_llava(
        examples,
        algorithm,
        task,
        num_graphs,
        use_text,
        use_image,
        seed,
):
    image_links = get_image_links(
        algorithm=algorithm,
        num_graphs=num_graphs,
        seed=seed,
    )
    white_image_link = get_image_links(
        algorithm=algorithm,
        num_graphs=num_graphs,
        seed=seed,
        white=True
    )
    postfix = format_postfix[task]

    messages = {}
    for key, example in examples.items():
        if use_text is True and use_image is False:
            _template = copy.deepcopy(
                llava_message_template["zero_shot_text"]
            )
            _template["content"][1]["text"] = example["question"] + postfix
            messages[key] = [
                _template,
                {
                    "image_url": white_image_link,
                }
            ]

        elif use_text is False and use_image is True:
            _template = copy.deepcopy(
                llava_message_template["zero_shot_image"]
            )
            _template["content"][1]["text"] = _template["content"][1]["text"].format(
                "\nQ:" + example["question"].split("\nQ:")[1]
            ) + postfix
            messages[key] = [
                _template,
                {
                    "image_url": image_links[int(key)],
                }
            ]

        elif use_text is True and use_image is True:
            _template = copy.deepcopy(
                llava_message_template["zero_shot_image"]
            )
            _template["content"][1]["text"] = _template["content"][1]["text"].format(
                example["question"]
            ) + postfix
            messages[key] = [
                _template,
                {
                    "image_url": image_links[int(key)],
                }
            ]

        else:
            raise ValueError("Invalid message option.")

    return messages


def zero_shot(
        examples,
        algorithm,
        task,
        num_graphs,
        use_text,
        use_image,
        llm_model,
        seed,
):
    if llm_model in ["gpt-4o", "gpt-4-turbo"]:
        messages = zero_shot_openai(
            examples=examples,
            algorithm=algorithm,
            task=task,
            num_graphs=num_graphs,
            use_text=use_text,
            use_image=use_image,
            seed=seed,
        )
    elif llm_model in ["llava-v1.6-mistral-7b-hf"]:
        messages = zero_shot_llava(
            examples=examples,
            algorithm=algorithm,
            task=task,
            num_graphs=num_graphs,
            use_text=use_text,
            use_image=use_image,
            seed=seed,
        )
    else:
        raise ValueError("Invalid LLM option.")

    return messages


def few_shot_openai(
        examples,
        algorithm,
        task,
        num_graphs,
        use_text,
        use_image,
        k,
        seed,
):
    instruction = system_instruction
    image_links = get_image_links(
        algorithm=algorithm,
        num_graphs=num_graphs,
        seed=seed,
    )
    postfix = format_postfix[task]

    messages = {}

    for key, example in examples.items():
        knowledge_question_list = []
        knowledge_answer_list = []
        for item in example["question"].split("Example: ")[1:][:-1]:
            knowledge_question_list.append(
                item.split("\nA: ")[0]
            )
            knowledge_answer_list.append(
                item.split("\nA: ")[1].split("\n")[0]
            )
        main_question = example["question"].split("Example: ")[-1]

        messages[key] = [
            instruction,
        ]
        if use_text is True and use_image is False:
            for i in range(k):
                _question = copy.deepcopy(
                    openai_message_template["few_shot_text"]["question"]
                )
                _answer = copy.deepcopy(
                    openai_message_template["few_shot_text"]["answer"]
                )
                _question["content"] = knowledge_question_list[i]
                _answer["content"] = knowledge_answer_list[i]
                messages[key].extend([_question, _answer])
            _template = copy.deepcopy(
                openai_message_template["few_shot_text"]["question"]
            )
            _template["content"] = main_question + postfix
            messages[key].append(_template)

        elif use_text is False and use_image is True:
            for i in range(k):
                _question = copy.deepcopy(
                    openai_message_template["few_shot_image"]["question"]
                )
                _answer = copy.deepcopy(
                    openai_message_template["few_shot_image"]["answer"]
                )
                _question["content"][0]["text"] = _question["content"][0]["text"].format(
                    "\nQ:" + knowledge_question_list[i].split("\nQ:")[1]
                )
                _question["content"][1]["image_url"]["url"] = image_links[int(key)]
                _answer["content"] = knowledge_answer_list[i]
                messages[key].extend([_question, _answer])
            _template = copy.deepcopy(
                openai_message_template["few_shot_image"]["question"]
            )
            _template["content"][0]["text"] = _template["content"][0]["text"].format(
                "\nQ:" + main_question.split("\nQ:")[1]
            ) + postfix
            _template["content"][1]["image_url"]["url"] = image_links[int(key)]
            messages[key].append(_template)

        elif use_text is True and use_image is True:
            for i in range(k):
                _question = copy.deepcopy(
                    openai_message_template["few_shot_text_image"]["question"]
                )
                _answer = copy.deepcopy(
                    openai_message_template["few_shot_text_image"]["answer"]
                )
                _question["content"][0]["text"] = _question["content"][0]["text"].format(
                    knowledge_question_list[i]
                )
                _question["content"][1]["image_url"]["url"] = image_links[int(key)]
                _answer["content"] = knowledge_answer_list[i]
                messages[key].extend([_question, _answer])
            _template = copy.deepcopy(
                openai_message_template["few_shot_text_image"]["question"]
            )
            _template["content"][0]["text"] = _template["content"][0]["text"].format(
                main_question
            ) + postfix
            _template["content"][1]["image_url"]["url"] = image_links[int(key)]
            messages[key].append(_template)

        else:
            raise ValueError("Invalid message option.")

    return messages


def few_shot_llava(
        examples,
        algorithm,
        task,
        num_graphs,
        use_text,
        use_image,
        k,
        seed,
):
    image_links = get_image_links(
        algorithm=algorithm,
        num_graphs=num_graphs,
        seed=seed,
    )
    white_image_link = get_image_links(
        algorithm=algorithm,
        num_graphs=num_graphs,
        seed=seed,
        white=True
    )
    postfix = format_postfix[task]

    messages = {}

    for key, example in examples.items():
        knowledge_question_list = []
        knowledge_answer_list = []
        for item in example["question"].split("Example: ")[1:][:-1]:
            knowledge_question_list.append(
                item.split("\nA: ")[0]
            )
            knowledge_answer_list.append(
                item.split("\nA: ")[1].split("\n")[0]
            )
        main_question = example["question"].split("Example: ")[-1]

        messages[key] = []
        if use_text is True and use_image is False:
            for i in range(k):
                _question = copy.deepcopy(
                    llava_message_template["few_shot_text"]["question"]
                )
                _answer = copy.deepcopy(
                    llava_message_template["few_shot_text"]["answer"]
                )
                _question["content"][1]["text"] = knowledge_question_list[i]
                _question["content"].append(
                    {
                        "image_url": white_image_link,
                    }
                )
                _answer["content"] = knowledge_answer_list[i]
                messages[key].extend([_question, _answer])
            _template = copy.deepcopy(
                llava_message_template["few_shot_text"]["question"]
            )
            _template["content"][1]["text"] = main_question + postfix
            messages[key].append(_template)
            messages[key].append(
                {
                    "image_url": white_image_link,
                }
            )

        elif use_text is False and use_image is True:
            for i in range(k):
                _question = copy.deepcopy(
                    llava_message_template["few_shot_image"]["question"]
                )
                _answer = copy.deepcopy(
                    llava_message_template["few_shot_image"]["answer"]
                )
                _question["content"][1]["text"] = _question["content"][1]["text"].format(
                    "\nQ:" + knowledge_question_list[i].split("\nQ:")[1]
                )
                _question["content"].append(
                    {
                        "image_url": image_links[int(key)],
                    }
                )
                _answer["content"] = knowledge_answer_list[i]
                messages[key].extend([_question, _answer])
            _template = copy.deepcopy(
                llava_message_template["few_shot_image"]["question"]
            )
            _template["content"][1]["text"] = _template["content"][1]["text"].format(
                "\nQ:" + main_question.split("\nQ:")[1]
            ) + postfix
            messages[key].append(_template)
            messages[key].append(
                {
                    "image_url": white_image_link,
                }
            )

        elif use_text is True and use_image is True:
            for i in range(k):
                _question = copy.deepcopy(
                    llava_message_template["few_shot_text_image"]["question"]
                )
                _answer = copy.deepcopy(
                    llava_message_template["few_shot_text_image"]["answer"]
                )
                _question["content"][1]["text"] = _question["content"][1]["text"].format(
                    knowledge_question_list[i]
                )
                _question["content"].append(
                    {
                        "image_url": image_links[int(key)],
                    }
                )
                _answer["content"] = knowledge_answer_list[i]
                messages[key].extend([_question, _answer])
            _template = copy.deepcopy(
                llava_message_template["few_shot_text_image"]["question"]
            )
            _template["content"][1]["text"] = _template["content"][1]["text"].format(
                main_question
            ) + postfix
            messages[key].append(_template)
            messages[key].append(
                {
                    "image_url": white_image_link,
                }
            )

        else:
            raise ValueError("Invalid message option.")

    return messages


def few_shot(
        examples,
        algorithm,
        task,
        num_graphs,
        use_text,
        use_image,
        llm_model,
        k,
        seed,
):
    if llm_model in ["gpt-4o", "gpt-4-turbo"]:
        messages = few_shot_openai(
            examples=examples,
            algorithm=algorithm,
            task=task,
            num_graphs=num_graphs,
            use_text=use_text,
            use_image=use_image,
            k=k,
            seed=seed,
        )
    elif llm_model in ["llava-v1.6-mistral-7b-hf"]:
        messages = few_shot_llava(
            examples=examples,
            algorithm=algorithm,
            task=task,
            num_graphs=num_graphs,
            use_text=use_text,
            use_image=use_image,
            k=k,
            seed=seed,
        )
    else:
        raise ValueError("Invalid LLM option.")

    return messages


def get_file_path(
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
):
    file_path = PurePath(
        project_root_path,
        "input",
        "generated_messages",
        provider,
        algorithm,
        text_encoder,
        # "{}-algo-{}-num_graphs-{}-text_encoder-{}-task-{}-cot-{}-bag-{}-text-{}-image-{}-seed-{}.json".format(
        "{}-{}-{}-{}-{}-{}-{}-{}-{}-{}.json".format(
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
    )

    return file_path


def check_messages(
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
):
    if llm_model in ["gpt-4o", "gpt-4-turbo"]:
        provider = "openai"
    elif llm_model in ["llava-v1.6-mistral-7b-hf"]:
        provider = "llava"
    else:
        raise ValueError("Invalid LLM option.")

    task_type = task_type + f"_{k}" if task_type == "few_shot" else task_type

    file_path = get_file_path(
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
    )

    if os.path.isfile(file_path):
        print(f"{file_path} has generated messages")
        return True
    else:
        return False


def save_messages(
        messages,
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
):
    if llm_model in ["gpt-4o", "gpt-4-turbo"]:
        provider = "openai"
    elif llm_model in ["llava-v1.6-mistral-7b-hf"]:
        provider = "llava"
    else:
        raise ValueError("Invalid LLM option.")

    task_type = task_type + f"_{k}" if task_type == "few_shot" else task_type

    file_path = get_file_path(
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
    )

    init_path(dir_or_file=file_path)
    with open(file_path, 'w') as file:
        json.dump(messages, file, indent=2)


def load_messages(
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
):
    if llm_model in ["gpt-4o", "gpt-4-turbo"]:
        provider = "openai"
    elif llm_model in ["llava-v1.6-mistral-7b-hf"]:
        provider = "llava"
    else:
        raise ValueError("Invalid LLM option.")

    task_type = task_type + f"_{k}" if task_type == "few_shot" else task_type

    file_path = get_file_path(
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
    )

    with open(file_path, 'r') as file:
        messages = json.load(file)

    return messages
