import os
from pathlib import PurePath

import random
import networkx as nx
import numpy as np

from code.utils import init_path, project_root_path


_NUMBER_OF_NODES_RANGE = {
    "small": np.arange(5, 10),
    "medium": np.arange(10, 15),
    "large": np.arange(15, 20),
}
_NUMBER_OF_COMMUNITIES_RANGE = {
    "small": np.arange(2, 4),
    "medium": np.arange(2, 8),
    "large": np.arange(2, 10),
}


def get_dir(
        algorithm,
        num_graphs,
        seed,
):
    output_dir = PurePath(
        project_root_path,
        "input",
        "generated_graphs",
        "algo-{}-num_graphs-{}-seed-{}".format(
            algorithm,
            num_graphs,
            seed,
        ),
    )

    return output_dir



def check_graphs(
        algorithm,
        num_graphs,
        seed,
):
    output_dir = get_dir(
        algorithm=algorithm,
        num_graphs=num_graphs,
        seed=seed,
    )
    if os.path.isdir(output_dir):
        print(f"{output_dir} has generated graphs")
        return True
    else:
        return False


def save_graphs(
        graphs,
        algorithm,
        num_graphs,
        seed,
):
    """Writes graphs to output_dir."""

    output_dir = get_dir(
        algorithm=algorithm,
        num_graphs=num_graphs,
        seed=seed,
    )
    init_path(dir_or_file=output_dir, is_dir=True)

    for ind, graph in enumerate(graphs):
        nx.write_graphml(
            graph,
            open(
                os.path.join(output_dir, str(ind) + ".graphml"), "wb",
            ),
        )


def load_graphs(
        algorithm,
        num_graphs,
        seed,

):
    """Writes graphs to output_dir."""

    # Graph dir
    graph_dir = get_dir(
        algorithm=algorithm,
        num_graphs=num_graphs,
        seed=seed,
    )

    loaded_graphs = []
    for file in os.listdir(graph_dir):
        if file.endswith('.graphml'):
            path = os.path.join(graph_dir, file)
            graph = nx.read_graphml(open(path, 'rb'), node_type=int)
            loaded_graphs.append(graph)
        else:
            print(f"{file} is not a graphml file")

    return loaded_graphs


def generate_graphs(
        number_of_graphs,
        algorithm,
        directed,
        random_seed = 1234,
        er_min_sparsity = 0.0,
        er_max_sparsity = 1.0,
):
    """Generating multiple graphs using the provided algorithms.

    Args:
      number_of_graphs: number of graphs to generate
      algorithm: the random graph generator algorithm
      directed: whether to generate directed or undirected graphs.
      random_seed: the random seed to generate graphs with.
      er_min_sparsity: minimum sparsity of er graphs.
      er_max_sparsity: maximum sparsity of er graphs.

    Returns:
      generated_graphs: a list of nx graphs.
    Raises:
      NotImplementedError: if the algorithm is not yet implemented.
    """

    random.seed(random_seed)
    np.random.seed(random_seed)

    generated_graphs = []
    graph_sizes = random.choices(
        list(_NUMBER_OF_NODES_RANGE.keys()), k=number_of_graphs
    )
    random_state = np.random.RandomState(random_seed)
    if algorithm == "er":
        for i in range(number_of_graphs):
            sparsity = random.uniform(er_min_sparsity, er_max_sparsity)
            number_of_nodes = random.choice(_NUMBER_OF_NODES_RANGE[graph_sizes[i]])
            generated_graphs.append(
                nx.erdos_renyi_graph(
                    number_of_nodes, sparsity, seed=random_state, directed=directed
                )
            )

    elif algorithm == "ba":
        for i in range(number_of_graphs):
            number_of_nodes = random.choice(_NUMBER_OF_NODES_RANGE[graph_sizes[i]])
            m = random.randint(1, number_of_nodes - 1)
            generated_graph = nx.barabasi_albert_graph(
                number_of_nodes, m, seed=random_state
            )
            if directed:
                generated_graphs.append(randomize_directions(generated_graph))
            else:
                generated_graphs.append(generated_graph)

    elif algorithm == "sbm":
        for i in range(number_of_graphs):
            number_of_nodes = random.choice(_NUMBER_OF_NODES_RANGE[graph_sizes[i]])
            number_of_communities = random.choice(
                _NUMBER_OF_COMMUNITIES_RANGE[graph_sizes[i]]
            )
            # sizes forms number of nodes in communities.
            sizes = []
            for _ in range(number_of_communities - 1):
                sizes.append(
                    random.randint(
                        1,
                        max(
                            1,
                            number_of_nodes - sum(sizes) - (number_of_communities - 1),
                        ),
                    )
                )
            sizes.append(number_of_nodes - sum(sizes))

            # p forms probabilities of communities connecting each other.
            p = np.random.uniform(size=(number_of_communities, number_of_communities))
            if random.uniform(0, 1) < 0.5:
                p = np.maximum(p, p.transpose())
            else:
                p = np.minimum(p, p.transpose())
            sbm_graph = nx.stochastic_block_model(
                sizes, p, seed=random_state, directed=directed
            )
            # sbm graph generator automatically adds dictionary attributes.
            sbm_graph = remove_graph_data(sbm_graph)
            generated_graphs.append(sbm_graph)

    elif algorithm == "sfn":
        for i in range(number_of_graphs):
            number_of_nodes = random.choice(_NUMBER_OF_NODES_RANGE[graph_sizes[i]])
            generated_graph = nx.scale_free_graph(number_of_nodes, seed=random_state)
            # sfn graphs are by default directed.
            if not directed:
                generated_graphs.append(remove_directions(generated_graph))
            else:
                generated_graphs.append(generated_graph)

    elif algorithm == "complete":
        for i in range(number_of_graphs):
            number_of_nodes = random.choice(_NUMBER_OF_NODES_RANGE[graph_sizes[i]])
            create_using = nx.DiGraph if directed else nx.Graph
            generated_graphs.append(
                nx.complete_graph(number_of_nodes, create_using=create_using)
            )

    elif algorithm == "star":
        for i in range(number_of_graphs):
            number_of_nodes = random.choice(_NUMBER_OF_NODES_RANGE[graph_sizes[i]])
            # number_of_nodes for star is the input + a center node.
            generated_graph = nx.star_graph(number_of_nodes - 1)
            if directed:
                generated_graphs.append(randomize_directions(generated_graph))
            else:
                generated_graphs.append(generated_graph)

    elif algorithm == "path":
        for i in range(number_of_graphs):
            number_of_nodes = random.choice(_NUMBER_OF_NODES_RANGE[graph_sizes[i]])
            create_using = nx.DiGraph if directed else nx.Graph
            generated_graphs.append(
                nx.path_graph(number_of_nodes, create_using=create_using)
            )

    else:
        raise NotImplementedError()
    return generated_graphs


def remove_graph_data(graph):
    # GraphML writer does not support dictionary data for nodes or graphs.
    for ind in range((graph.number_of_nodes())):
        graph.nodes[ind].pop("block", None)
    graph_data_keys = list(graph.graph.keys())
    for _, node in enumerate(graph_data_keys):
        graph.graph.pop(node, None)
    return graph


def randomize_directions(graph):
    # Converting the undirected graph to a directed graph.
    directed_graph = graph.to_directed()
    # For each edge, randomly choose a direction.
    edges = list(graph.edges())
    for u, v in edges:
        if random.random() < 0.5:
            directed_graph.remove_edge(u, v)
        else:
            directed_graph.remove_edge(v, u)

    return directed_graph


def remove_directions(graph):
    # Converting the direted graph to an undirected one by removing directions.
    undirected_graph = nx.Graph()
    undirected_graph.add_nodes_from(graph.nodes())
    # Add edges between nodes, ignoring directions.
    for u, v in graph.edges():
        undirected_graph.add_edge(u, v)

    return undirected_graph
