def answer(words):

    graph = build_graph(words)
    start = start_nodes(graph)

    letters = []
    visited = []

    # this is a depth first graph traversal algorithm
    def visit(node):
        if node not in visited:
            visited.append(node)

            if node in graph:
                for edge in graph[node]:
                    visit(edge)

            # have found next letter of the alphabet :simple_smile:
            letters.append(node)

    # visit every starting node, depth first
    for node in start:
        visit(node)

    # minglish complete
    return ''.join(letters[::-1])


def build_graph(words):

    # start with empty graph
    # nodes are key, edges are values
    graph = {}

    rows = len(words)

    # the plan here is to take pairs of words with indices
    # 0,1 -> 1,2 -> 2,3
    for row in range(rows - 1):

        # find an edge (relationship) between two words
        edge = find_edge(words[row], words[row + 1])

        if edge is not None:
            # a valid edge could be determined,
            # so add it to the graph

            node, direction = edge

            if node in graph:

                # node already exists in the graph, so just add the edge
                graph[node].append(direction)
            else:

                # node doesn't exist yet, so create it first
                graph[node] = [direction]

    return graph


def find_edge(a, b):

    # minimum length of the two strings,
    length = min(len(a), len(b))

    # keep checking across the two words
    # until the letters are different, ie. a an edge can be created
    for c in range(length):
        if a[c] != b[c]:
            return a[c], b[c]


def start_nodes(graph):
    """
    We need to find starting nodes of the graph, which are nodes which were
    never on the right side of a relationship, ie. if we know that 'x' < 'y',
    then 'y' can not be a starting node.
    To determine this set of starting nodes we need to traverse the graph
    and only include nodes which are not present in any of the edges.
    """

    # all edges
    e = set()

    for edges in graph.values():
        for edge in edges:
            e.add(edge)

    # starting nodes
    s = set()

    for node in graph:
        if node not in e:
            s.add(node)

    return s
