import os
from pathlib import PurePath

import numpy as np
import json

from code.utils import init_path, project_root_path


def create_zero_shot_task(
        task,
        graphs,
        generator_algorithm,
        text_encoder,
        cot,
        bag,
):
    examples_dict = task.prepare_examples_dict(
        graphs=graphs,
        generator_algorithm=generator_algorithm,
        encoding_method=text_encoder
    )
    if cot:
        for key in examples_dict.keys():
            examples_dict[key]['question'] += "Let's think step by step. "
    if bag:
        for key in examples_dict.keys():
            examples_dict[key]['question'] = examples_dict[key]['question'].replace(
                '\nQ: ',
                "\nLet's construct the graph with the nodes and edges first.\nQ: ",
            )  # pytype: disable=attribute-error

    return examples_dict


def zero_shot(
        task,
        graphs,
        algorithm,
        text_encoder,
        cot,
        bag,
):
    examples = create_zero_shot_task(
        task=task,
        graphs=graphs,
        generator_algorithm=algorithm,
        text_encoder=text_encoder,
        cot=cot,
        bag=bag,
    )

    return examples


def prepare_few_shots(
        task,
        graphs,
        text_encoder,
        cot,
):
    """Create a dict of few-shot examples with their cot for the task."""
    few_shots_examples_dict = {}

    if text_encoder not in few_shots_examples_dict:
        few_shots_examples_dict[(text_encoder)] = []
    for graph in graphs:
        few_shots_examples_dict[(text_encoder)].append(
            task.create_few_shot_example(graph, text_encoder, cot)
        )

    return few_shots_examples_dict


def choose_few_shot_examples(
        target_ind,
        few_shots_dict,
        encoding_method,
        k,
):
    # """Choose few shot examples for each algorithm."""
    # few_shots_str = ''
    # for _ in range(k):
    #     example_list = few_shots_dict[encoding_method]
    #     few_shots_str += 'Example: ' + random.choice(example_list) + '\n'
    # return few_shots_str

    """Choose few shot examples and return example IDs."""
    few_shots_str = ''
    example_list = few_shots_dict[encoding_method]
    few_shots_inds = np.random.choice(len(example_list), k).tolist()
    while target_ind in few_shots_inds:
        few_shots_inds = np.random.choice(len(example_list), k).tolist()
    for ind in few_shots_inds:
        few_shots_str += 'Example: ' + example_list[ind] + '\n'
    return few_shots_str, few_shots_inds


def create_few_shot_task(
        task,
        graphs,
        generator_algorithm,
        k,
        text_encoder,
        cot,
        bag,
):
    """Create a recordio file with few-shot examples for the task."""
    # print('prepare few shot task', 'cot', cot, 'bag', bag)
    few_shots_examples_dict = prepare_few_shots(
        task=task,
        graphs=graphs,
        text_encoder=text_encoder,
        cot=cot,
    )

    examples_dict = task.prepare_examples_dict(
        graphs=graphs, generator_algorithm=generator_algorithm,
        encoding_method=text_encoder
    )
    for key in examples_dict.keys():
        few_shots_examples, few_shots_inds = choose_few_shot_examples(
            target_ind=int(key),
            few_shots_dict=few_shots_examples_dict,
            encoding_method=text_encoder,
            k=k,
        )
        examples_dict[key]['question'] = (
            few_shots_examples + 'Example: ' + examples_dict[key]['question']
        )
        if bag:
            examples_dict[key]['question'] = examples_dict[key]['question'].replace(
                '\nQ: ',
                "\nLet's construct the graph with the nodes and edges first.\nQ: ",
            )  # pytype: disable=attribute-error
        examples_dict[key]['few_shot_graph_ids'] = few_shots_inds

    return examples_dict


def few_shot(
        task,
        graphs,
        algorithm,
        text_encoder,
        cot,
        bag,
        k,
):
    examples = create_few_shot_task(
        task=task,
        graphs=graphs,
        generator_algorithm=algorithm,
        k=k,
        text_encoder=text_encoder,
        cot=cot,
        bag=bag,
    )

    return examples


def get_file_path(
        task_type,
        algorithm,
        num_graphs,
        text_encoder,
        task_name,
        cot,
        bag,
        seed,
):
    file_path = PurePath(
        project_root_path,
        "input",
        "generated_examples",
        algorithm,
        text_encoder,
        # "{}-algo-{}-num_graphs-{}-text_encoder-{}-task-{}-cot-{}-bag-{}-seed-{}.json".format(
        "{}-{}-{}-{}-{}-{}-{}-{}.json".format(
            task_type,
            algorithm,
            num_graphs,
            text_encoder,
            task_name,
            str(cot),
            str(bag),
            seed,
        ),
    )

    return file_path


def check_examples(
        task_type,
        algorithm,
        num_graphs,
        text_encoder,
        task_name,
        cot,
        bag,
        k,
        seed,
):
    task_type = task_type + f"_{k}" if task_type == "few_shot" else task_type

    file_path = get_file_path(
        task_type=task_type,
        algorithm=algorithm,
        num_graphs=num_graphs,
        text_encoder=text_encoder,
        task_name=task_name,
        cot=cot,
        bag=bag,
        seed=seed,
    )

    if os.path.isfile(file_path):
        print(f"{file_path} has generated examples")
        return True
    else:
        return False


def save_examples(
        examples,
        task_type,
        algorithm,
        num_graphs,
        text_encoder,
        task_name,
        cot,
        bag,
        k,
        seed,
):
    task_type = task_type + f"_{k}" if task_type == "few_shot" else task_type

    file_path = get_file_path(
        task_type=task_type,
        algorithm=algorithm,
        num_graphs=num_graphs,
        text_encoder=text_encoder,
        task_name=task_name,
        cot=cot,
        bag=bag,
        seed=seed,
    )

    init_path(dir_or_file=file_path)
    with open(file_path, 'w') as file:
        json.dump(examples, file, indent=2)


def load_examples(
        task_type,
        algorithm,
        num_graphs,
        text_encoder,
        task_name,
        cot,
        bag,
        k,
        seed,
):
    task_type = task_type + f"_{k}" if task_type == "few_shot" else task_type

    file_path = get_file_path(
        task_type=task_type,
        algorithm=algorithm,
        num_graphs=num_graphs,
        text_encoder=text_encoder,
        task_name=task_name,
        cot=cot,
        bag=bag,
        seed=seed,
    )

    with open(file_path, 'r') as file:
        examples = json.load(file)

    return examples
