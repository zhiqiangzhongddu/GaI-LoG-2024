from code.config import cfg, update_cfg
from code.task_generator_utils import load_examples
from code.message_generator_utils import zero_shot, few_shot, check_messages, save_messages


def generate_and_save_messages(
        cfg,
):
    if not check_messages(
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
    ):
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

        if cfg.task.type == "zero_shot":
            messages = zero_shot(
                examples=examples,
                algorithm=cfg.graph.algorithm,
                task=cfg.task.name,
                num_graphs=cfg.graph.num_graphs,
                use_text=cfg.task.use_text,
                use_image=cfg.task.use_image,
                llm_model=cfg.llm.name,
                seed=cfg.seed,
            )
        elif cfg.task.type == "few_shot":
            messages = few_shot(
                examples=examples,
                algorithm=cfg.graph.algorithm,
                task=cfg.task.name,
                num_graphs=cfg.graph.num_graphs,
                use_text=cfg.task.use_text,
                use_image=cfg.task.use_image,
                llm_model=cfg.llm.name,
                k=cfg.task.k,
                seed=cfg.seed,
            )
        else:
            raise NotImplementedError

        save_messages(
            messages=messages,
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
    else:
        pass


def main(cfg):
    assert not cfg.task.use_text == cfg.task.use_image == False, "use_text {}, use_image {}".format(
        cfg.task.use_text, cfg.task.use_image
    )
    print(
        f"Generating messages: algorithm {cfg.graph.algorithm} "
        f"text_encoder {cfg.task.text_encoder} task {cfg.task.name} type {cfg.task.type} "
        f"cot {str(cfg.task.cot)} bag {str(cfg.task.bag)} "
        f"use_text {str(cfg.task.use_text)} use_image {str(cfg.task.use_image)}"
    )

    generate_and_save_messages(cfg=cfg)


if __name__ == "__main__":
    cfg = update_cfg(cfg)

    cfg.graph.num_graphs = 500 if cfg.graph.algorithm in ["er", "ba", "sbm", "sfn"] else 100
    main(cfg)
