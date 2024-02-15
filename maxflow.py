# Source: https://brilliant.org/wiki/ford-fulkerson-algorithm/#residual-graphs

class Vertex:
    def __init__(self, name, source=False, sink=False):
        self.name = name
        self.source = source
        self.sink = sink

class Edge:
    def __init__(self, _from, to, capacity):
        self._from = _from
        self.to = to
        self.capacity = capacity
        self.flow = 0
        self.returnEdge = None

class FlowNetwork:
    def __init__(self):
        self.vertices = []
        self.network = {}

    def getSource(self):
        for vertex in self.vertices:
            if vertex.source:
                return vertex
        return None
    
    def setSource(self, V):
        self.vertices[V].source = True
    
    def getSink(self):
        for vertex in self.vertices:
            if vertex.sink:
                return vertex
        return None

    def setSink(self, V):
        self.vertices[V].sink = True

    def getVertex(self, V):
        for vertex in self.vertices:
            if vertex.name == V:
                return vertex
        return None

    def vertexInNetwork(self, V):
        for vertex in self.vertices:
            if vertex.name == V:
                return True
        return False
    
    def getEdges(self):
        allEdges = []
        for vertex in self.network:
            for edge in self.network[vertex]:
                allEdges.append(edge)
        
        return allEdges
    
    def addVertex(self, name, source, sink):
        if (sink==True and source==True):
            print("Error: Same vertex can't sink and source")
            return
        if(self.vertexInNetwork(name)):
            print("Error: Vertex already exists in network")
            return
        if(source==True):
            if(self.getSource() != None):
                print("Error: Source already exists")
                return
        if(sink==True):
            if(self.getSink() != None):
                print("Error: Sink already exists")
                return
            
        newVertex = Vertex(name=name, source=source, sink=sink)
        self.vertices.append(newVertex)
        self.network[newVertex.name] = []

    def addEdge(self, _from, to, capacity):
        if (_from == to):
            return "Error: Can't have same from and to Vertex"
        if (self.vertexInNetwork(_from) == False):
            return "Error: From vertex doesn't exist in network"
        if (self.vertexInNetwork(to) == False):
            return "Error: To vertex doesn't exist in network"
        
        newEdge = Edge(_from=_from, to=to, capacity=capacity)
        returnEdge = Edge(_from=to, to=_from, capacity=0)
        newEdge.returnEdge = returnEdge

        vertex = self.getVertex(_from)
        self.network[vertex.name].append(newEdge)

        returnVertex = self.getVertex(to)
        self.network[returnVertex.name].append(returnEdge)

    def getPath(self, _from, to, path):
        if(_from == to):
            return path

        for edge in self.network[_from]:
            residualCapacity = edge.capacity - edge.flow
            if residualCapacity > 0 and not (edge, residualCapacity) in path:
                result = self.getPath(edge.to, to, path + [(edge, residualCapacity)])
                if result != None:
                    return result

    def calculateMaxFlow(self):
        source = self.getSource()
        sink = self.getSink()
        
        if source == None or sink == None:
            return "Network does not have source and sink"
        
        path = self.getPath(source.name, sink.name, [])

        while path != None:
            flow = min(edge[1] for edge in path)
            for edge, res in path:
                edge.flow += flow
                if edge.returnEdge != None:
                    edge.returnEdge.flow -= flow
            path = self.getPath(source.name, sink.name, [])
        return sum(edge.flow for edge in self.network[source.name])