from code import graph_task
from code.graph_generator_utils import load_graphs
from code.config import cfg, update_cfg
from code.task_generator_utils import zero_shot, few_shot, check_examples, save_examples


TASK_CLASS = {
    'edge_existence': graph_task.EdgeExistence,
    'node_degree': graph_task.NodeDegree,
    'node_count': graph_task.NodeCount,
    'edge_count': graph_task.EdgeCount,
    'connected_nodes': graph_task.ConnectedNodes,
    'cycle_check': graph_task.CycleCheck,
    'disconnected_nodes': graph_task.DisconnectedNodes,
    'reachability': graph_task.Reachability,
    'shortest_path': graph_task.ShortestPath,
    'maximum_flow': graph_task.MaximumFlow,
    'triangle_counting': graph_task.TriangleCounting,
}


def generate_and_save_tasks(
        cfg,
        task,
):
    if not check_examples(
            task_type=cfg.task.type,
            algorithm=cfg.graph.algorithm,
            num_graphs=cfg.graph.num_graphs,
            text_encoder=cfg.task.text_encoder,
            task_name=cfg.task.name,
            cot=cfg.task.cot,
            bag=cfg.task.bag,
            k=cfg.task.k,
            seed=cfg.seed,
    ):
        # load test graphs
        graphs = load_graphs(
            algorithm=cfg.graph.algorithm,
            num_graphs=cfg.graph.num_graphs,
            seed=cfg.seed,
        )

        if cfg.task.type == "zero_shot":
            examples = zero_shot(
                task=task,
                graphs=graphs,
                algorithm=cfg.graph.algorithm,
                text_encoder=cfg.task.text_encoder,
                cot=cfg.task.cot,
                bag=cfg.task.bag,
            )
        elif cfg.task.type == "few_shot":
            examples = few_shot(
                task=task,
                graphs=graphs,
                algorithm=cfg.graph.algorithm,
                text_encoder=cfg.task.text_encoder,
                cot=cfg.task.cot,
                bag=cfg.task.bag,
                k=cfg.task.k,
            )
        else:
            raise NotImplementedError

        save_examples(
            examples=examples,
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
    else:
        pass


def main(cfg):
    print(
        f"Generating tasks: algorithm {cfg.graph.algorithm} "
        f"text_encoder {cfg.task.text_encoder} task {cfg.task.name} "
        f"cot {str(cfg.task.cot)} bag {str(cfg.task.bag)}"
    )

    # Defining a task on the graphs
    task = TASK_CLASS[cfg.task.name]()

    cfg.task.type = "zero_shot"
    generate_and_save_tasks(cfg, task)

    cfg.task.type = "few_shot"
    generate_and_save_tasks(cfg, task)


if __name__ == "__main__":
    cfg = update_cfg(cfg)

    cfg.graph.num_graphs = 500 if cfg.graph.algorithm in ["er", "ba", "sbm", "sfn"] else 100
    main(cfg)
