import random


class Graph:
    def __init__(self, nr_of_vertices=0):
        self.__out = {}
        self.__in = {}
        self.__cost = {}

        for i in range(nr_of_vertices):
            self.__out[i] = []
            self.__in[i] = []

    def is_vertex(self, x):
        if x not in self.__in:
            return False
        return True

    def get_nr_of_vertices(self):
        return len(self.__in)

    def parse_vertices(self):
        return list(self.__out.keys())

    def is_edge(self, x, y):
        if not self.is_vertex(x) or not self.is_vertex(y):
            return False
        if y not in self.__out[x]:
            return False
        if x not in self.__in[y]:
            return False
        return True

    def get_in_degree(self, x):
        if not self.is_vertex(x):
            raise Exception('Vertex does not exists')

        return len(self.__in[x])

    def get_out_degree(self, x):
        if not self.is_vertex(x):
            raise Exception('Vertex does not exists')

        return len(self.__out[x])

    def get_inbound_edges(self, vertex):
        if not self.is_vertex(vertex):
            raise Exception('Vertex does not exists')

        in_edges = []
        for in_vertex in self.__in[vertex]:
            in_edges.append(in_vertex)

        return in_edges

    def get_outbound_edges(self, vertex):
        if not self.is_vertex(vertex):
            raise Exception('Vertex does not exists')

        out_edges = []
        for out_vertex in self.__out[vertex]:
            out_edges.append(out_vertex)

        return out_edges

    def get_cost_of_edge(self, x, y):
        if not self.is_edge(x, y):
            raise Exception('Edge does not exist')

        return self.__cost[(x, y)]

    def modify_cost_of_edge(self, x, y, new_cost):
        if not self.is_edge(x, y):
            raise Exception('Edge does not exist')

        self.__cost[(x, y)] = new_cost

    def add_vertex(self, x):
        if self.is_vertex(x):
            raise Exception('Vertex already exists')

        self.__in[x] = []
        self.__out[x] = []

    def remove_vertex(self, x):
        if not self.is_vertex(x):
            raise Exception('Vertex does not exists')

        for vertex in self.__in[x]:
            self.__out[vertex].remove(x)
            del self.__cost[(vertex, x)]

        for vertex in self.__out[x]:
            self.__in[vertex].remove(x)
            del self.__cost[(x, vertex)]

        del self.__in[x]
        del self.__out[x]

    def add_edge(self, x, y, cost):
        if self.is_edge(x, y):
            raise Exception('Edge already exists')

        self.__out[x].append(y)
        self.__in[y].append(x)
        self.__cost[(x, y)] = cost

    def remove_edge(self, x, y):
        if not self.is_edge(x, y):
            raise Exception('Edge does not exist')

        self.__in[y].remove(x)
        self.__out[x].remove(y)
        del self.__cost[(x, y)]

    def get_edges(self):
        edges = []

        for vertex in self.parse_vertices():
            for out_vertex in self.get_outbound_edges(vertex):
                edges.append((vertex, out_vertex, self.__cost[(vertex, out_vertex)]))
        return edges

    def copy_graph(self):
        graph_copy = Graph(0)

        for vertex in self.parse_vertices():
            graph_copy.add_vertex(vertex)

        for vertex in self.parse_vertices():
            for in_vertex in self.__in[vertex]:
                graph_copy.add_edge(in_vertex, vertex, self.__cost[in_vertex, vertex])

        return graph_copy


def read_from_file_2(filename):
    with(open(filename, "r")) as f:
        vertices, edges = f.readline().split()
        vertices = int(vertices)
        edges = int(edges)
        graph = Graph()
        for line in range(vertices):
            data = f.readline().split()
            graph.add_vertex(int(data[0]))

        for line in range(edges):
            data = f.readline().split()
            x = int(data[0])
            y = int(data[1])
            cost = int(data[2])
            graph.add_edge(x, y, cost)

    f.close()
    return graph


def read_from_file(filename):
    with(open(filename, "r")) as f:
        vertices, edges = f.readline().split()
        vertices = int(vertices)
        edges = int(edges)
        graph = Graph(vertices)

        for line in range(edges):
            data = f.readline().split()
            x = int(data[0])
            y = int(data[1])
            cost = int(data[2])
            graph.add_edge(x, y, cost)

    f.close()
    return graph


def write_to_file(filename, graph: Graph):
    with(open(filename, "w")) as f:
        nr_vertices = graph.get_nr_of_vertices()
        all_edges = graph.get_edges()
        nr_edges = len(all_edges)
        f.write(f'{nr_vertices} {nr_edges} \n')
        all_vertices = graph.parse_vertices()
        for vertex in range(nr_vertices):
            f.write(f'{all_vertices[vertex]}\n')
        for edge in all_edges:
            f.write(f'{edge[0]} {edge[1]} {edge[2]}\n')

    f.close()


def create_random_graph(n, m):
    g = Graph(nr_of_vertices=n)
    if m > n * n:
        raise Exception('too many vertices')
    number_of_added_edges = 0
    # failed_attempts_at_adding_an_edge = 0
    while number_of_added_edges < m:
        x = random.randrange(n)
        y = random.randrange(n)
        cost = random.randint(-10, 10)
        try:
            g.add_edge(x, y, cost)
            number_of_added_edges += 1
        except Exception:
            continue
        # else:
        # failed_attempts_at_adding_an_edge += 1
    # print(f'There were {failed_attempts_at_adding_an_edge} failed attempts')
    return g


