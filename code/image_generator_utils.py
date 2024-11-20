import os
from pathlib import PurePath

import networkx as nx
from tqdm import tqdm
import requests
import matplotlib.pyplot as plt

from code.utils import init_path, project_root_path


def plot_and_save_fig(
        graph,
        show=True,
        save=False,
        file_path=""
):
    # Draw the graph with enhancements
    plt.figure(figsize=(12, 12))  # Increase the figure size for better clarity
    pos = nx.spring_layout(graph)  # Choose a layout

    options = {
        "font_size": 15,
        "node_size": 500,
        "node_color": "white",
        "edgecolors": "black",
        "linewidths": 1,
        "width": 1,
    }
    nx.draw_networkx(graph, pos, **options)

    # Set margins for the axes so that nodes aren't clipped
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")

    if show:
        plt.show()

    if save:
        # Save the drawn graph as an image file
        plt.savefig(
            file_path,
            dpi=300,
            bbox_inches='tight',
            format='png',
            transparent=True,
        )

    plt.close()


def generate_and_save_images(
        graphs,
        algorithm,
        num_graphs,
        seed,
):
    # Graph image dir
    graph_image_dir = PurePath(
        project_root_path,
        "input",
        "generated_images",
        "algo-{}-num_graphs-{}-seed-{}".format(
            algorithm,
            num_graphs,
            seed,
        ),
    )
    init_path(dir_or_file=graph_image_dir, is_dir=True)

    display = f"Generating graph images {algorithm}"
    for ind, graph in enumerate(tqdm(graphs, desc=display)):
        file_path = os.path.join(
            graph_image_dir,
            f"{ind}.png"
        )
        if not os.path.isfile(file_path):
            plot_and_save_fig(
                graph=graph,
                show=False,
                save=True,
                file_path=file_path
            )
        else:
            pass


def is_image_url(url):
    try:
        response = requests.head(url, allow_redirects=True)
        content_type = response.headers.get('Content-Type', '').lower()
        if 'image' in content_type:
            return True
        else:
            return False
    except requests.RequestException as e:
        print(f"Error checking URL: {e}")
        return False


def get_image_links(
        algorithm,
        num_graphs,
        seed,
        white=False
):
    if white:
        return "https://raw.githubusercontent.com/zhiqiangzhongddu/GaI-Image/main/white.png"
    else:
        link_template = "https://raw.githubusercontent.com/zhiqiangzhongddu/GaI-Image/main/algo-{}-num_graphs-{}-seed-{}/{}.png"

        links = []
        for ind in range(num_graphs):
            link = link_template.format(
                algorithm,
                num_graphs,
                seed,
                ind,
            )
            # Link check is too slow
            # if is_image_url(link):
            #     links.append(link)
            # else:
            #     raise ValueError(f"Invalid image link: {link}")
            links.append(link)

        return links
