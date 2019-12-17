# adjacency matrix implementation


class Vertex:

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbors(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getID(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):

        return str(self.id) + ' connected To ' + str([x.id for x in self.connectedTo])


class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        print(newVertex)
        return newVertex

    def getVertex(self, n):

        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def addEdge(self, fromVertex, toVertex, cost=0):

        if fromVertex not in self.vertList:
            nv = self.addVertex(fromVertex)

        if toVertex not in self.vertList:
            nv = self.addVertex(addVertex)

        self.vertList[fromVertex].addNeighbors(self.vertList[toVertex], cost)
        print(self.vertList[fromVertex])

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def __contains__(self, n):
        return n in self.vertList


g = Graph()

for i in range(5):
    g.addVertex(i)


g.addEdge(0, 1, 2)
# g.addEdge(0,1,2)
# g.addEdge(0,1,2)
# g.addEdge(0,1,2)
# g.addEdge(0,1,2)
# g.addEdge(0,1,2)
# g.addEdge(0,1,2)
# g.addEdge(0,1,2)
# g.addEdge(0,1,2)


for vertex in g:
    print(vertex)
    print(vertex.getConnections())
    print('\n')
