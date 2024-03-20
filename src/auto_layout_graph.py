from manim import *
from src.vertex import Vertex
from src.edge import Edge


def getGraphAsMobjects(vertices, edges, capacities, layout_scale=2, layout="spring"):
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
        print(x, y)
        vertex = Vertex(str(i), x, y, 1)
        verticesAsObjects.update({i: vertex})

    for _from, to, capacity in capacities:
        edge = Edge(verticesAsObjects.get(_from), verticesAsObjects.get(to), capacity)
        edgesAsObjects.append(edge)

    return verticesAsObjects.values(), edgesAsObjects


def getMaxCapacity(capacities):
    return max(capacities, key=lambda x: x[2])[2]
