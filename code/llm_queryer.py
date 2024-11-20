from code.config import cfg, update_cfg
from code.message_generator_utils import load_messages
from code.llm_queryer_utils import check_responses, query_llm, save_responses


def query_llm_and_save(
        cfg,
):
    if not check_responses(
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
    ):
        message_list = list(load_messages(
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
        ).values())

        if cfg.demo_test:
            cfg.task.name = "demo_" + cfg.task.name
            message_list = message_list[:cfg.num_sample]

        responses = query_llm(
            message_list=message_list,
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
            gpu_id=cfg.gpu_id,
        )

        save_responses(
            responses=responses,
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
    else:
        pass


def main(cfg):
    assert not cfg.task.use_text == cfg.task.use_image == False, "use_text {}, use_image {}".format(
        cfg.task.use_text, cfg.task.use_image
    )
    print(
        f"Querying: llm {cfg.llm.name} "
        f"algorithm {cfg.graph.algorithm} task {cfg.task.name} "
        f"type {cfg.task.type} text_encoder {cfg.task.text_encoder} "
        f"cot {str(cfg.task.cot)} bag {str(cfg.task.bag)} "
        f"use_text {str(cfg.task.use_text)} use_image {str(cfg.task.use_image)}"
    )

    query_llm_and_save(cfg=cfg)


if __name__ == "__main__":
    cfg = update_cfg(cfg)

    cfg.graph.num_graphs = 500 if cfg.graph.algorithm in ["er", "ba", "sbm", "sfn"] else 100
    main(cfg)
