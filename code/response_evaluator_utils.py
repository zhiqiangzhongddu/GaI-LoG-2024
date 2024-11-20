import re
import sys


def answer_keyword_extractor(
        input_string,
        task,
):
    input_string = input_string["answer"].lower()

    if task in ["edge_existence", "cycle_check"]:
        return "yes" if "yes" in input_string else "no"

    elif task in ["node_degree", "node_count", "edge_count", "triangle_counting", "shortest_path"]:
        return re.findall(r'\d+', input_string)[0]

    elif task in ["connected_nodes"]:
        return input_string

    else:
        raise NotImplementedError


def extract_node_degree_openai(input_string):
    # Convert the input string to lowercase
    input_string = input_string.lower()

    # Define a regular expression pattern to match the degree
    pattern = re.compile(
        r"The degree is\s*\[?(\d+)\]?|degree of node \d+ is\s*\[?(\d+)\]?".lower(),
        re.IGNORECASE
    )

    # Search for the pattern in the string
    match = re.search(pattern, input_string)
    if match:
        return match.group(1)
    else:
        # print(0, input_string)
        return "Input string matching error."


def extract_node_degree_llava(input_string):
    # Convert the input string to lowercase
    input_string = input_string.lower()

    # Define a regular expression pattern to match the degree of a node
    pattern = re.compile(
        r"degree of node \d+ (?:in the (?:graph|image) )?is (\d+)".lower(),
        re.IGNORECASE
    )

    # Search for the pattern in the string
    match = re.search(pattern, input_string)
    if match:
        return match.group(1)
    else:
        return "Input string matching error."


def extract_node_count(
        input_string
):
    # Convert the input string to lowercase
    input_string = input_string.lower()

    # Define a regular expression pattern to match the number of nodes
    pattern = re.compile(
        r"The number of nodes in (?:the|this)? graph is\s*\[?(\d+)\]?".lower(),
        re.IGNORECASE
    )

    # Search for the pattern in the string
    match = re.search(pattern, input_string)
    if match:
        return match.group(1)
    else:
        return "Input string matching error."


def extract_edge_count(
        input_string
):
    # Convert the input string to lowercase
    input_string = input_string.lower()

    # Define a regular expression pattern to match the number of nodes
    pattern = re.compile(
        r"The number of edges in (?:the|this)? graph is\s*\[?(\d+)\]?".lower(),
        re.IGNORECASE
    )

    # Search for the pattern in the string
    match = re.search(pattern, input_string)
    if match:
        return match.group(1)
    else:
        return "Input string matching error."


def extract_connected_nodes(
        input_string
):
    # Convert the input string to lowercase
    input_string = input_string.lower()

    # Define a regular expression pattern to match the nodes
    pattern = re.compile(
        r"The connected nodes (?:to (?:\d+|node \d+) )?in alphabetical order are:\s*\[?([\d,\s]+)\]?\.?".lower(),
        re.IGNORECASE
    )

    # Search for the pattern in the string
    match = re.search(pattern, input_string)
    if match:
        nodes = ""
        for node in match.group(1).split(','):
            nodes += node.strip() + ", "
        return nodes[:-2] + "."
    else:
        return "Input string matching error."

def extract_triangle_counting(
        input_string
):
    # Convert the input string to lowercase
    input_string = input_string.lower()

    # Define a regular expression pattern to match the nodes
    pattern = re.compile(
        r"The number of triangles in (?:the|this)? graph is\s*\[?(\d+)\]?".lower(),
        re.IGNORECASE
    )

    # Search for the pattern in the string
    match = re.search(pattern, input_string)
    if match:
        return match.group(1)
    else:
        return "Input string matching error."


def extract_shortest_path_openai(
        input_string
):
    # Convert the input string to lowercase
    input_string = input_string.lower()

    # Define a regular expression pattern to match the nodes
    pattern = re.compile(
        r"The length of (?:the|this)? shortest path is\s*\[?(\d+)\]?".lower(),
        re.IGNORECASE
    )

    # Search for the pattern in the string
    match = re.search(pattern, input_string)
    if match:
        return match.group(1)
    else:
        return "Input string matching error."


def extract_shortest_path_llava(
        input_string
):
    # Convert the input string to lowercase
    input_string = input_string.lower()

    # Define a regular expression pattern to match the shortest path information
    pattern = re.compile(
        r"(?:the length of the shortest path from node \d+ to node \d+(?: (?:in the given|in this) (?:undirected graph|image))? is|the shortest path from node \d+ to node \d+ (?:in the given|in this) (?:undirected graph|image) is) (\d+)",
        re.IGNORECASE
    )

    # Search for the pattern in the string
    match = re.search(pattern, input_string)
    if match:
        return match.group(1)
    else:
        return "Input string matching error."


def response_keyword_extractor(
        llm_provider,
        input_string,
        task,
):
    input_string = input_string.lower()

    if llm_provider == "openai":
        pass
    elif llm_provider == "llava":
        input_string = input_string.split("[/INST]".lower())[1]
        input_string = input_string.split("Q:".lower())[0] \
            if "Q:".lower() in input_string else input_string
    else:
        raise NotImplementedError
    # print("input_string: ", input_string)

    if task == "edge_existence":
        if "Yes, there is an edge".lower() in input_string:
            return "yes"
        elif "No, there is not an edge".lower() in input_string:
            return "no"
        else:
            return "uncertain"
    
    elif task == "cycle_check":
        if "Yes, there is a cycle".lower() in input_string:
            return "yes"
        elif "yes, there is a cycle in this graph".lower() in input_string:
            return "yes"
        elif "No, there is no cycle".lower() in input_string:
            return "no"
        else:
            return "uncertain"

    elif task == "node_degree":
        if llm_provider == "openai":
            return extract_node_degree_openai(input_string)
        elif llm_provider == "llava":
            return extract_node_degree_llava(input_string)
        else:
            raise NotImplementedError

    elif task == "node_count":
        return extract_node_count(input_string)

    elif task == "edge_count":
        return extract_edge_count(input_string)

    elif task == "connected_nodes":
        return extract_connected_nodes(input_string)

    elif task == "triangle_counting":
        return extract_triangle_counting(input_string)

    elif task == "shortest_path":
        if llm_provider == "openai":
            return extract_shortest_path_openai(input_string)
        elif llm_provider == "llava":
            return extract_shortest_path_llava(input_string)
        else:
            raise NotImplementedError

    else:
        sys.exit("Input task matching error.")
