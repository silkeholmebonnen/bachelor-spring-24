from manim import *
from src.vertex import Vertex
from src.edge import Edge


def getEdgesAndVerticesAsMobjects(
    vertices, edges, capacities, layout_scale=2, layout="spring", layers=[]
):
    partitions = getPartitions(layers)
    graph = []
    if partitions != []:
        graph = Graph(
            vertices,
            edges,
            layout_scale=layout_scale,
            layout="partite",
            partitions=partitions,
        )
    else:
        graph = Graph(
            vertices,
            edges,
            layout_scale=layout_scale,
            layout=layout,
            layout_config={"seed": 100},
        )

    verticesAsObjects = {}
    edgesAsObjects = []

    for dot, i in enumerate(graph.vertices):
        x, y, _ = graph._layout[dot]
        vertex = Vertex(str(i), x, y, 1)
        verticesAsObjects.update({i: vertex})

    for _from, to, capacity in capacities:
        edge = Edge(verticesAsObjects.get(_from), verticesAsObjects.get(to), capacity)
        edgesAsObjects.append(edge)

    return verticesAsObjects.values(), edgesAsObjects


def getPartitions(layers):
    partitions = []
    c = -1

    for i in layers:
        partitions.append(list(range(c + 1, c + i + 1)))
        c += i

    return partitions


def getMaxCapacity(capacities):
    return max(capacities, key=lambda x: x[2])[2]


def getMinVertexCapacity(vertices: list[Vertex]):
    return min(vertices, key=lambda x: x.max_capacity).max_capacity
