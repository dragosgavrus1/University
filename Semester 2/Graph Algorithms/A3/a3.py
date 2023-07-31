from graph import Graph
import heapq
import graph


def min_path_dp(g: Graph, s, t):
    # d[k][x] = cost of min cost walk from s to x of length = k
    # if no such walk exists, then x will not be a key in d[k]

    # check if the vertexes exist
    if not g.is_vertex(s) or not g.is_vertex(t):
        raise Exception("Vertexes are invalid")

    # Initialize a list to store the distances for each k (length of the walk)
    d = [{x: float('inf') for x in g.parse_vertices()}]
    d[0][s] = 0  # Set the distance from the start vertex to itself as 0
    n = len(g.parse_vertices())

    modify = True
    # Calculate the minimum distance for each k from 1 to n-1 (n is the number of vertices in the graph)
    for k in range(1, n):
        if modify is True:
            modify = False
            curr_dist = d[-1]  # Get the distances for the previous k
            next_dist = d[-1].copy()  # Initialize the distances for the current k
            for x in g.parse_vertices():
                for y in g.get_inbound_edges(x):
                    # Update the distance for vertex x if there is a shorter path from vertex y to x
                    if next_dist[x] > curr_dist[y] + g.get_cost_of_edge(y, x):
                        next_dist[x] = curr_dist[y] + g.get_cost_of_edge(y, x)
                        modify = True
            d.append(next_dist)
        else:
            break

    # Check if there is a negative cost cycle in the graph
    for x in g.parse_vertices():
        for y in g.get_inbound_edges(x):
            if d[-1][x] > g.get_cost_of_edge(y, x) + d[-1][y]:
                raise Exception("Negative cost cycle detected!")

    # Find the k with the minimum distance to the target vertex
    best_k = None
    for k in range(len(d)):
        if best_k is None or d[k][t] < d[best_k][t]:
            best_k = k

    # If there is no path to the target vertex, raise an exception
    if d[best_k][t] == float('inf') or best_k == 0:
        raise Exception("There is no path")

    print(f"Length={best_k}, Cost={d[best_k][t]}")

    # Find the shortest walk from the start to the target vertex
    walk = []
    while best_k > 0:
        walk.append(t)  # add t to walk
        for p in g.get_inbound_edges(t):
            # Check if the distance to the current vertex in the previous k plus the cost of the edge
            # from the previous vertex to the current vertex is equal to the distance to the current vertex in the
            # current k
            if d[best_k - 1][p] + g.get_cost_of_edge(p, t) == d[best_k][t]:
                t = p
                best_k -= 1
                break

    walk.append(s)  # Add the start vertex to the walk
    walk.reverse()  # Reverse the walk to get it in the correct order
    return walk

