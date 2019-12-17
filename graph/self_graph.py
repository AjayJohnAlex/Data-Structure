from collections import defaultdict

graph = defaultdict(list)


def addEdge(graph, source, destination):

    graph[source].append(destination)


def generate_graph(graph):

    edges = []

    for vertices in graph:

        for connected_vertices in graph[vertices]:

            edges.append((vertices, connected_vertices))

    return edges


addEdge(graph, 'a', 'b')
addEdge(graph, 'b', 'c')

print(generate_graph(graph))
