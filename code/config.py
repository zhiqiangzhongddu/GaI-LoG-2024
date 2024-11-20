import os
import argparse
from yacs.config import CfgNode as CN


def set_cfg(cfg):

    # ------------------------------------------------------------------------ #
    # Basic options
    # ------------------------------------------------------------------------ #
    # Whether to use Demo Test mode
    cfg.demo_test = False
    # Number of samples for demo test
    cfg.num_sample = 10
    # Fix the running seed to remove randomness
    cfg.seed = 42
    # GPU ID
    cfg.gpu_id = 0
    # Parameters to generate graphs
    cfg.graph = CN()
    # Parameters to generate tasks
    cfg.task = CN()
    # Parameters to query LLM
    cfg.llm = CN()

    # ------------------------------------------------------------------------ #
    # Graph Generation options
    # ------------------------------------------------------------------------ #
    # Number of graphs
    cfg.graph.num_graphs = 0
    # Algorithm to generate graphs
    cfg.graph.algorithm = "er"
    # Whether generate directed graphs
    cfg.graph.directed = False
    # Min sparsity of the generated graphs
    cfg.graph.er_min_sparsity = 0.0
    # Max sparsity of the generated graphs
    cfg.graph.er_max_sparsity = 1.0

    # ------------------------------------------------------------------------ #
    # Task Generation options
    # ------------------------------------------------------------------------ #
    # Task name
    # edge_existence, node_degree, node_count, edge_count, connected_nodes,
    # cycle_check, disconnected_nodes, reachability, shortest_path,
    # maximum_flow, triangle_counting, node_classification,
    cfg.task.name = "cycle_check"
    # zero-shot, few-shot
    cfg.task.type = "zero_shot"
    # Name of Text Encoder
    # adjacency, incident, friendship, south_park, got, politician, social_network
    # expert, coauthorship, random
    cfg.task.text_encoder = "adjacency"
    # Whether adopt cot settings
    cfg.task.cot = False
    # Whether adopt bag settings
    cfg.task.bag = False
    # Number of samples for few-shot
    cfg.task.k = 2
    # Question use graph text
    cfg.task.use_text = False
    # Question use graph image
    cfg.task.use_image = False

    # # ------------------------------------------------------------------------ #
    # # LLM provider options
    # # ------------------------------------------------------------------------ #
    # #
    # cfg.llm.provider = "openai"

    # ------------------------------------------------------------------------ #
    # LLM Model options
    # ------------------------------------------------------------------------ #
    # LLM model name
    # gpt-4o, gpt-4-turbo, llava-v1.6-mistral-7b-hf
    cfg.llm.name = "llava-v1.6-mistral-7b-hf"
    cfg.llm.temperature = 1.
    cfg.llm.top_p = 1.
    cfg.llm.frequency_penalty = 0.
    cfg.llm.presence_penalty = 0.
    # temperature: Defaults to 1 (suggest 0.6?)
    #               What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
    #               make the output more random, while lower values like 0.2 will make it more
    #               focused and deterministic.
    # top_p: Defaults to 1 (suggest 0.9?)
    #               An alternative to sampling with temperature, called nucleus sampling, where the
    #               model considers the results of the tokens with top_p probability mass. So 0.1
    #               means only the tokens comprising the top 10% probability mass are considered.
    #               We generally recommend altering this or `top_p` but not both.
    # frequency_penalty: Defaults to 0
    #               Number between -2.0 and 2.0. Positive values penalize new tokens based on their
    #               existing frequency in the text so far, decreasing the model's likelihood to
    #               repeat the same line verbatim.
    # presence_penalty: Defaults to 0
    #               Number between -2.0 and 2.0. Positive values penalize new tokens based on
    #               whether they appear in the text so far, increasing the model's likelihood to
    #               talk about new topics.
    #               [See more information about frequency and presence penalties.]
    #               (https://platform.openai.com/docs/guides/text-generation/parameter-details)

    return cfg


# Principle means that if an option is defined in a YACS config object,
# then your program should set that configuration option using cfg.merge_from_list(opts) and not by defining,
# for example, --train-scales as a command line argument that is then used to set cfg.TRAIN.SCALES.


def update_cfg(cfg, args_str=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="",
                        metavar="FILE", help="Path to config file")
    # opts arg needs to match set_cfg
    parser.add_argument("opts", default=[], nargs=argparse.REMAINDER,
                        help="Modify config options using the command-line")

    if isinstance(args_str, str):
        # parse from a string
        args = parser.parse_args(args_str.split())
    else:
        # parse from command line
        args = parser.parse_args()
    # Clone the original cfg
    cfg = cfg.clone()

    # Update from config file
    if os.path.isfile(args.config):
        cfg.merge_from_file(args.config)

    # Update from command line
    cfg.merge_from_list(args.opts)

    return cfg


"""
    Global variable
"""
cfg = set_cfg(CN())

