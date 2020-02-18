from graph import Graph, Stack, Queue

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])
    oldest = graph.dft_farthest(starting_node)

    if oldest == None:
        return -1
    else:
        return oldest
