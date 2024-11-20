from code.config import cfg, update_cfg
from code.task_generator_utils import load_examples
from code.message_generator_utils import load_messages
from code.llm_queryer_utils import load_responses
from code.response_evaluator_utils import answer_keyword_extractor, response_keyword_extractor

if cfg.graph.algorithm in ["er", "ba", "sbm", "sfn"]:
    cfg.graph.num_graphs = 500
elif cfg.graph.algorithm in ["complete", "star", "path"]:
    cfg.graph.num_graphs = 100
else:
    raise NotImplementedError()


cfg.llm.name = "llava-v1.6-mistral-7b-hf" # gpt-4o, gpt-4-turbo llava-v1.6-mistral-7b-hf
cfg.task.type = "few_shot"
# edge_existence, node_degree, node_count, edge_count, connected_nodes,
# cycle_check, disconnected_nodes, reachability, shortest_path,
# maximum_flow, triangle_counting, node_classification,
# cfg.task.name = "cycle_check"
# adjacency, incident, friendship, south_park, got, politician, social_network, expert, coauthorship, random
cfg.task.text_encoder = "incident"
cfg.task.cot = True
cfg.task.bag = True
cfg.task.use_text = True
cfg.task.use_image = True

if cfg.llm.name in ["gpt-4o", "gpt-4-turbo"]:
    llm_provider = "openai"
elif cfg.llm.name in ["llava-v1.6-mistral-7b-hf"]:
    llm_provider = "llava"
else:
    raise NotImplementedError()

for task_name in [
    "edge_existence", "node_degree", "node_count",
    "edge_count", "connected_nodes", "cycle_check",
    "triangle_counting", "shortest_path"
]:
# for task_name in [
#     "shortest_path"
# ]:
    cfg.task.name = task_name

    messages = load_messages(
        task_type=cfg.task.type,
        algorithm=cfg.graph.algorithm,
        num_graphs=cfg.graph.num_graphs,
        text_encoder=cfg.task.text_encoder,
        task_name=cfg.task.name,
        cot=cfg.task.cot,
        bag=cfg.task.bag,
        use_text=cfg.task.use_text,
        use_image=cfg.task.use_image,
        k=cfg.task.k,
        llm_model=cfg.llm.name,
        seed=cfg.seed,
    )
    examples = load_examples(
        task_type=cfg.task.type,
        algorithm=cfg.graph.algorithm,
        num_graphs=cfg.graph.num_graphs,
        text_encoder=cfg.task.text_encoder,
        task_name=cfg.task.name,
        cot=cfg.task.cot,
        bag=cfg.task.bag,
        k=cfg.task.k,
        seed=cfg.seed,
    )
    responses = load_responses(
        llm_model=cfg.llm.name,
        task_type=cfg.task.type,
        algorithm=cfg.graph.algorithm,
        num_graphs=cfg.graph.num_graphs,
        text_encoder=cfg.task.text_encoder,
        task_name=cfg.task.name,
        cot=cfg.task.cot,
        bag=cfg.task.bag,
        use_text=cfg.task.use_text,
        use_image=cfg.task.use_image,
        k=cfg.task.k,
        seed=cfg.seed,
        demo_test=cfg.demo_test,
    )

    correct_num = 0
    for idx, (example, response) in enumerate(zip(examples.values(), responses.values())):
        answer_keyword = answer_keyword_extractor(
            input_string=example,
            task=cfg.task.name,
        )
        response_keyword = response_keyword_extractor(
            llm_provider=llm_provider,
            input_string=response,
            task=cfg.task.name,
        )

        # if response_keyword == "Input string matching error.":
        #     print(0, idx, answer_keyword, response_keyword, response)

        if answer_keyword == response_keyword:
            correct_num += 1
        else:
            # print("paris: ", idx, "\n", answer_keyword, "\n", response_keyword, "\n", response)
            # if response_keyword == "Input string matching error.":
            #     print("paris: ", idx, "\n", answer_keyword, "\n", response_keyword, "\n", response)
            pass
    print(round(correct_num / len(responses) * 100, 1), "&")