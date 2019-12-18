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

# finding the path between 2 vertices


def findPath(graph, start, end, path=[]):

    path = path + [start]
    if start == end:
        return path

    for vertice in graph[start]:
        if vertice not in path:
            newpath = findPath(graph, vertice, end, path)
            # if newpath:
            return newpath
            # return None


def shortest_path(graph, start, end, path=[]):

    path = path + [start]
    if start == end:
        return path
    shortestPath = None
    for vertices in graph[start]:
        if vertices not in path:
            print('path', path)
            newpath = shortest_path(graph, vertices, end, path)
            print('newpath', newpath)
            # if newpath:
            #     if not shortestPath or len(newpath) < len(shortestPath):
            #         shortestPath = newpath

    return newpath


addEdge(graph, 'a', 'c')
addEdge(graph, 'b', 'd')
addEdge(graph, 'a', 'd')
# addEdge(graph, 'c', 'e')
addEdge(graph, 'd', 'a')
addEdge(graph, 'd', 'f')
# addEdge(graph, 'e', 'b')
# addEdge(graph, 'e', 'c')
addEdge(graph, 'c', 'e')
addEdge(graph, 'e', 'f')

# print(generate_graph(graph))
# print(findPath(graph, 'a', 'f'))
print(graph.items())
print(shortest_path(graph, 'a', 'f'))
# print(find_shortest_path(graph, 'a', 'f'))
