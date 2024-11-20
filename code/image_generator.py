from code.config import cfg, update_cfg
from code.graph_generator_utils import load_graphs
from code.image_generator_utils import generate_and_save_images
from code.utils import set_seed


def main(cfg):
    print(f"Generating images for algorithm {cfg.graph.algorithm}")
    graphs = load_graphs(
        algorithm=cfg.graph.algorithm,
        num_graphs=cfg.graph.num_graphs,
        seed=cfg.seed,
    )
    generate_and_save_images(
        graphs=graphs,
        algorithm=cfg.graph.algorithm,
        num_graphs=cfg.graph.num_graphs,
        seed=cfg.seed,
    )


if __name__ == "__main__":
    cfg = update_cfg(cfg)
    set_seed(cfg.seed)

    cfg.graph.num_graphs = 500 if cfg.graph.algorithm in ["er", "ba", "sbm", "sfn"] else 100
    main(cfg)
