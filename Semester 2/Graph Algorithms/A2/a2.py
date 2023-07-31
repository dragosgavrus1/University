from graph import Graph


def bfs1(graph: Graph, s):
    """
    Executes a Breadth-First Search in graph g starting from vertex s.
    Returns a dictionary where the keys are all the accessible vertices from s
    and the value for a vertex x is the shortest walk from s to x as a list of vertices
    """
    queue = [s]
    walks = {s: [s]}  # shortest walk
    while len(queue) != 0:
        vertex = queue.pop(0)  # get the first vertex from the queue
        for outbound in graph.get_outbound_edges(vertex):
            if outbound not in walks:  # if there is no shortest path yet
                walks[outbound] = walks[vertex] + [outbound]  # shortest path to the parent vertex and the outbound
                queue.append(outbound)  # add the outbound of the vertex to the end to check it because it is accessible

    return walks


def shortest_path1(graph: Graph, s, t):
    """
    Computes the shortest (min length) walk from vertex s to vertex t in graph g.
    Returns the list of vertices along the walk. Returns None if no walk exists.
    """
    walks = bfs1(graph, s)
    if t not in walks.keys():
        return None
    return walks[t]  # shortest path from s to t
