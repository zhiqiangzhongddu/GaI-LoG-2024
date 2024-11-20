system_instruction = {
    "role": "system",
    "content":
        "You are an AI designed to analyze graphs and answer "
        "specific questions about the graphs. You will receive "
        "an image containing a graph and a textual description "
        "of the graph's structure. Based on the visual and "
        "textual information, you should provide accurate answers "
        "to the provided questions.",
}

# edge_existence, node_degree, node_count, edge_count, connected_nodes,
# cycle_check, disconnected_nodes, reachability, shortest_path,
# maximum_flow, triangle_counting, node_classification,
format_postfix = {
    "edge_existence": "Answer the question using this format: Yes, there is an edge./No, there is not an edge.",
    "cycle_check": "Answer the question using this format: Yes, there is a cycle./No, there is no cycle.",
    "reachability": "Answer the question using this format: Yes, there is a path./No, there is not a path.",
    "node_degree": "Answer the question using this format: The degree is [].",
    "node_count": "Answer the question using this format: The number of nodes in the graph is [].",
    "edge_count": "Answer the question using this format: The number of edges in the graph is [].",
    "connected_nodes": "Answer the question using this format: The connected nodes in alphabetical order are: [].",
    "disconnected_nodes": "Answer the question using this format: The disconnected nodes in alphabetical order are: [].",
    "shortest_path": "Answer the question using this format: The length of the shortest path is [].",
    "maximum_flow": "Answer the question using this format: The maximum capacity of the flow is [].",
    "triangle_counting": "Answer the question using this format: The number of triangles in the graph is [].",
}


openai_message_template = {
    "zero_shot_text": {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "There is an undirected graph in this image. {}",
            },
        ],
    },

    "zero_shot_image": {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "There is an undirected graph in this image. {}",
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": "",
                    "detail": "auto",
                },
            },
        ],
    },

    "zero_shot_text_image": {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "There is an undirected graph in this image. {}",
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": "",
                    "detail": "auto",
                },
            },
        ],
    },

    "few_shot_text": {
        "question": {
            "role": "user",
            "content": "{}",
        },
        "answer": {
            "role": "assistant",
            "content": "",
        },
    },

    "few_shot_image": {
        "question": {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "There is an undirected graph in this image. {}",
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "",
                        "detail": "auto",
                    },
                },
            ],
        },
        "answer": {
            "role": "assistant",
            "content": "",
        },
    },

    "few_shot_text_image": {
        "question": {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "There is an undirected graph in this image. {}",
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "",
                        "detail": "auto",
                    },
                },
            ],
        },
        "answer": {
            "role": "assistant",
            "content": "",
        },
    },
}

llava_message_template = {
    "zero_shot_text": {
        "role": "user",
        "content": [
            {
                "type": "image",
            },
            {
                "type": "text",
                "text": "",
            }
        ],
    },

    "zero_shot_image": {
        "role": "user",
        "content": [
            {
                "type": "image",
            },
            {
                "type": "text",
                "text": "There is an undirected graph in this image. {}",
            },
        ],
    },

    "zero_shot_text_image": {
        "role": "user",
        "content": [
            {
                "type": "image",
            },
            {
                "type": "text",
                "text": "There is an undirected graph in this image. {}",
            },
        ],
    },

    "few_shot_text": {
        "question": {
            "role": "user",
            "content": [
                {
                    "type": "image",
                },
                {
                    "type": "text",
                    "text": ""
                },
            ],
        },
        "answer": {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": ""
                }
            ],
        },
    },

    "few_shot_image": {
        "question": {
            "role": "user",
            "content": [
                {
                    "type": "image"
                },
                {
                    "type": "text",
                    "text": "There is an undirected graph in this image. {}"
                },
            ],
        },
        "answer": {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": ""
                }
            ],
        },
    },

    "few_shot_text_image": {
        "question": {
            "role": "user",
            "content": [
                {
                    "type": "image"
                },
                {
                    "type": "text",
                    "text": "There is an undirected graph in this image. {}"
                },
            ],
        },
        "answer": {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": ""
                }
            ],
        },
    },
}