from code.config import cfg, update_cfg
from code.graph_generator_utils import generate_graphs, check_graphs, save_graphs
from code.utils import set_seed


def main(cfg):
    if not check_graphs(
        algorithm=cfg.graph.algorithm,
        num_graphs=cfg.graph.num_graphs,
        seed=cfg.seed,
    ):
        print(f"Generating graphs: algorithm {cfg.graph.algorithm}")
        generated_graphs = generate_graphs(
            number_of_graphs=cfg.graph.num_graphs,
            algorithm=cfg.graph.algorithm,
            directed=cfg.graph.directed,
            random_seed=cfg.seed,
            er_min_sparsity=cfg.graph.er_min_sparsity,
            er_max_sparsity=cfg.graph.er_max_sparsity,
        )
        save_graphs(
            graphs=generated_graphs,
            algorithm=cfg.graph.algorithm,
            num_graphs=cfg.graph.num_graphs,
            seed=cfg.seed,
        )
    else:
        pass


if __name__ == "__main__":
    cfg = update_cfg(cfg)
    set_seed(cfg.seed)

    cfg.graph.num_graphs = 500 if cfg.graph.algorithm in ["er", "ba", "sbm", "sfn"] else 100
    main(cfg)
