from graph import *
from a2 import *
from a3 import *
from a4 import *


class UI:
    def __init__(self):
        pass

    @staticmethod
    def print_menu():
        print("\n")
        print("1. Get the number of vertices")
        print("2. Parse the vertices")
        print("3. Check if an edge exists")
        print("4. Degree in of vertex ")
        print("5. Degree out of vertex ")
        print("6. Print inbound edges ")
        print("7. Print outbound edges")
        print("8. Retrieve the information of an edge")
        print("9. Modify the information of an edge ")
        print("10. Add vertex ")
        print("11. Remove vertex")
        print("12. Add edge")
        print("13. Remove edge")
        print("14. Read a big graph example from a text file")
        print("15. Read a graph from a text file")
        print("16. Write a graph to a text file")
        print("17. Create a random graph")
        print("18. Get shortest length path between two vertices")
        print("19. Get the shortest cost path between two vertices")
        print("20. Topological sort and highest cost bath between 2 vertices")
        print("0. Exit")

    def run(self):
        graph = read_from_file_2('saved_graph.txt')
        while True:
            self.print_menu()
            option = input('Option: ')
            print("")

            if option == '0':
                exit()

            elif option == '1':
                print(f'The number of vertices is {graph.get_nr_of_vertices()}')

            elif option == '2':
                vertices = graph.parse_vertices()
                print('The vertices in the graph are: ', end="")
                for vertex in vertices:
                    print(f"{vertex} ", end="")
                print("")

            elif option == '3':
                x = input('First vertex: ')
                y = input('Second vertex: ')

                try:
                    x = int(x)
                    y = int(y)
                except ValueError:
                    print('Vertices should be integers')

                if graph.is_edge(x, y):
                    print(f'Edge {x},{y} exists.')
                else:
                    print(f'Edge {x},{y} does not exist.')

            elif option == '4':
                vertex = input('Vertex: ')
                try:
                    vertex = int(vertex)
                except ValueError:
                    print('Vertex should be integer')

                try:
                    print(f'In degree: {graph.get_in_degree(vertex)}')
                except Exception as e:
                    print(e)

            elif option == '5':
                vertex = input('Vertex: ')
                try:
                    vertex = int(vertex)
                except ValueError:
                    print('Vertex should be integer')

                try:
                    print(f'Out degree: {graph.get_out_degree(vertex)}')
                except Exception as e:
                    print(e)

            elif option == '6':
                vertex = input('Vertex: ')
                try:
                    vertex = int(vertex)
                except ValueError:
                    print('Vertex should be integer')

                try:
                    edges = graph.get_inbound_edges(vertex)
                    print('Inbound edges are: ', end="")
                    for i in edges:
                        print(i, end=" ")
                    print("")
                except Exception as e:
                    print(e)

            elif option == '7':
                vertex = input('Vertex: ')
                try:
                    vertex = int(vertex)
                except ValueError:
                    print('Vertex should be integer')

                try:
                    edges = graph.get_outbound_edges(vertex)
                    print('Outbound edges are: ', end="")
                    for i in edges:
                        print(i, end=" ")
                    print("")
                except Exception as e:
                    print(e)

            elif option == '8':
                x = input('First vertex: ')
                y = input('Second vertex: ')

                try:
                    x = int(x)
                    y = int(y)
                except ValueError:
                    print('Vertices should be integers')

                try:
                    cost = graph.get_cost_of_edge(x, y)
                    print(f'Cost of edge: {cost}')
                except Exception as e:
                    print(e)

            elif option == '9':
                x = input('First vertex: ')
                y = input('Second vertex: ')
                new_cost = input('New cost: ')
                try:
                    x = int(x)
                    y = int(y)
                    new_cost = int(new_cost)
                except ValueError:
                    print('Vertices should be integers')

                try:
                    graph.modify_cost_of_edge(x, y, new_cost)
                    print('Modify successful')
                except Exception as e:
                    print(e)

            elif option == '10':
                vertex = input('Vertex: ')
                try:
                    vertex = int(vertex)
                except ValueError:
                    print('Vertex should be integer')

                try:
                    graph.add_vertex(vertex)
                    print('Vertex added successfully')
                except Exception as e:
                    print(e)

            elif option == '11':
                vertex = input('Vertex: ')
                try:
                    vertex = int(vertex)
                except ValueError:
                    print('Vertex should be integer')

                try:
                    graph.remove_vertex(vertex)
                    print('Vertex removed successfully')
                except Exception as e:
                    print(e)

            elif option == '12':
                x = input('First vertex: ')
                y = input('Second vertex: ')
                cost = input('Cost: ')

                try:
                    x = int(x)
                    y = int(y)
                    cost = int(cost)
                except ValueError:
                    print('Vertices should be integers')

                try:
                    graph.add_edge(x, y, cost)
                    print('Edge added successfully')
                except Exception as e:
                    print(e)

            elif option == '13':
                x = input('First vertex: ')
                y = input('Second vertex: ')

                try:
                    x = int(x)
                    y = int(y)
                except ValueError:
                    print('Vertices should be integers')

                try:
                    graph.remove_edge(x, y)
                    print('Edge removed successfully')
                except Exception as e:
                    print(e)

            elif option == '14':
                filename = input('File name: ')

                try:
                    graph = read_from_file(filename)
                    print('Graph read successfully')
                except IOError:
                    print('Error reading')

            elif option == '15':
                filename = input('File name: ')

                try:
                    graph = read_from_file_2(filename)
                    print('Graph read successfully')
                except IOError:
                    print('Error reading')

            elif option == '16':
                filename = input('File name: ')

                try:
                    write_to_file(filename, graph)
                    print('Graph written successfully')
                except IOError:
                    print('Error writing')

            elif option == '17':
                vertices = input('Number of vertices: ')
                edges = input('Number of edges: ')

                try:
                    vertices = int(vertices)
                    edges = int(edges)
                except ValueError:
                    print("Number of vertices and edges should be integer")

                try:
                    graph = create_random_graph(vertices, edges)
                    print('Random graph generated')
                except Exception as e:
                    print(e)

            elif option == '18':
                start = input('Starting vertex: ')
                end = input('End vertex: ')

                try:
                    start = int(start)
                    end = int(end)
                except ValueError:
                    print('Vertices should be integers')

                result = shortest_path1(graph, start, end)
                if result is None:
                    print('There is no path')
                else:
                    print(f'Length: {len(result) - 1}')
                    print('Path: ', end=" ")
                    for vertex in result:
                        print(f'{vertex}', end=' ')
                    print("")

            elif option == '19':
                start = input('Starting vertex: ')
                end = input('End vertex: ')

                try:
                    start = int(start)
                    end = int(end)
                except ValueError:
                    print('Vertices should be integers')

                try:
                    walk = min_path_dp(graph, start, end)
                    print('Path: ', end=" ")
                    for vertex in walk:
                        print(f'{vertex}', end=' ')
                    print("")
                except Exception as e:
                    print(e)

            elif option == '20':
                start = input('Starting vertex: ')
                end = input('End vertex: ')

                try:
                    start = int(start)
                    end = int(end)
                except ValueError:
                    print('Vertices should be integers')

                try:
                    path, max_cost = highest_cost_path(graph, start, end)
                    if path is not None:
                        print(f'Max cost path: {max_cost}')
                        print('Path: ', end=" ")
                        for vertex in path:
                            print(f'{vertex}', end=' ')
                        print("")
                    else:
                        print('No path')
                except Exception as e:
                    print(e)
