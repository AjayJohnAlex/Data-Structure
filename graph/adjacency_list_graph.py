'''
Creating a Graph from adjacency list
'''


class Vertex(object):

    def __init__(self, n):
        self.name = n
        self.neighbors = list()

    def add_neighbors(self, neighbor):

        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
            self.neighbors.sort()


class Graph(object):

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_Edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbors(v)
                if key == v:
                    value.add_neighbors(u)

            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))


g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))

for i in range(ord('A'), ord('K')):
    g.add_vertex((Vertex(chr(i))))


edges = ['AB', 'AE', 'BF', 'CD', 'DE', 'EF']

for edge in edges:
    g.add_Edge(edge[:1], edge[:1])


g.print_graph()
