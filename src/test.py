from manim import *
from src.graph import FlowGraph
from src.auto_layout_graph import getGraphAsMobjects
from src.vertices_examples import VerticesExamples as V


class Test(Scene):
    def construct(self):
        vertices, edges, capacities = V.Silke()
        vertices, edges = getGraphAsMobjects(
            vertices, edges, capacities, layout_scale=3.5
        )
        graph = FlowGraph(vertices, edges)
        self.camera.background_color = WHITE
        # self.camera.frame_width = scale * 4
        # self.camera.resize_frame_shape(0)

        self.add(graph)


class Test2(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
        g = Graph(vertices, edges)
        self.add(g)
