from manim import *
from src.graph import FlowGraph
from src.auto_layout_graph import (
    getEdgesAndVerticesAsMobjects,
    getMaxCapacity,
    getMinVertexCapacity,
)
from src.vertices_examples import VerticesExamples as V


class Test(Scene):
    def construct(self):
        vertices, edges, capacities = V.SedgewickWayne()
        lt = {
            0: [-2, 0, 0],
            1: [-1, 1, 0],
            2: [-1, -1, 0],
            3: [1, 1, 0],
            4: [1, -1, 0],
            5: [2, 0, 0],
        }

        edgeScale = getMaxCapacity(capacities)
        vertices, edges = getEdgesAndVerticesAsMobjects(
            vertices, edges, capacities, layout_scale=edgeScale, layout=lt
        )

        vertexScale = getMinVertexCapacity(vertices)
        print(vertexScale, edgeScale)

        graph = FlowGraph(vertices, edges, vertexScale)
        self.camera.background_color = WHITE
        self.camera.frame_width = edgeScale * 4
        self.camera.resize_frame_shape(0)

        self.add(graph)


class Test2(Scene):
    def construct(self):
        vertices, edges, capacities = V.KleinbergTardos()
        edgeScale = getMaxCapacity(capacities)
        vertices, edges = getEdgesAndVerticesAsMobjects(
            vertices, edges, capacities, layout_scale=edgeScale
        )

        vertexScale = getMinVertexCapacity(vertices)
        print(vertexScale, edgeScale)

        graph = FlowGraph(vertices, edges, vertexScale)
        self.camera.background_color = WHITE
        self.camera.frame_width = edgeScale * 4
        self.camera.resize_frame_shape(0)

        self.add(graph)
