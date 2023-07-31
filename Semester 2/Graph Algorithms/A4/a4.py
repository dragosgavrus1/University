from collections import defaultdict

from graph import Graph


def dfs_with_cycle(g: Graph, current_vertex, sorted_vertices, visited):
    visited.add(current_vertex)
    for inbound in g.get_inbound_edges(current_vertex):
        if inbound not in visited:
            # Recursive call to perform depth-first traversal
            cycle = dfs_with_cycle(g, inbound, sorted_vertices, visited)
            if cycle is not None:
                if cycle[-1] == cycle[0]:
                    return cycle
                cycle.append(current_vertex)
                return cycle
        elif inbound not in sorted_vertices:
            return [inbound, current_vertex]

    sorted_vertices.append(current_vertex)
    return None


def highest_cost_path(g: Graph, source, destination):

    if not g.is_vertex(source) or not g.is_vertex(destination):
        raise Exception("Vertexes are invalid")

    sorted_vertices = []
    visited = set()

    # Topological sorting to ensure graph is a DAG
    for vertex in g.parse_vertices():
        if vertex not in visited:
            cycle = dfs_with_cycle(g, vertex, sorted_vertices, visited)
            if cycle is not None:
                print(f"Found the following cycle: {cycle}.")
                return None, None

    # Print the topological sort
    print("Topological sort: ", end="")
    for vertex in sorted_vertices:
        print(vertex, end=" ")
    print()

    distances = defaultdict(lambda: float('-inf'))
    prev = {}
    distances[source] = 0

    for vertex in sorted_vertices:
        for neighbour in g.get_outbound_edges(vertex):
            new_distance = distances[vertex] + g.get_cost_of_edge(vertex, neighbour)
            if new_distance > distances[neighbour]:
                distances[neighbour] = new_distance
                prev[neighbour] = vertex

    if distances[destination] == float('-inf'):
        return None, None

    path = []
    current_vertex = destination
    while current_vertex != source:
        path.append(current_vertex)
        current_vertex = prev[current_vertex]

    return path, distances[destination]
