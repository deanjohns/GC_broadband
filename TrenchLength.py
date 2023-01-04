import networkx as nx  # type:ignore


def getTrenchLength(tree, source, target):
    length = 0
    path = nx.shortest_path(tree, source, target)
    for i in range(len(path) - 1):
        sourceEdge = path[i]
        destinationEdge = path[i + 1]
        edge_length = tree.get_edge_data(sourceEdge, destinationEdge)["length"]
        length += edge_length
    return length
