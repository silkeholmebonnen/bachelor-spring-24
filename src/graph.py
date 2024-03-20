from manim import *
from src.edge import Edge
from src.vertex import Vertex


class FlowGraph(VMobject):
    def __init__(self, vertices, edges):
        super().__init__()
        self.vertices = vertices
        self.edges = edges

        for vertex in vertices:
            self.add(vertex)
            vertex.draw()

        for edge in edges:
            self.add(edge)
            edge.draw()


class Ex(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame_width = 30
        self.camera.resize_frame_shape(0)
        self.edges = {}
        self.vertices = {}

        self.add_vertices(
            [
                ["0", -5, 2, 8],
                ["3", 0, 0, 8],
                ["2", 5, 2, 8],
                ["1", -2, -3, 4],
                ["4", 3, -3, 4],
            ]
        )

        self.add_edges(
            [
                ["edge0_to_1", self.vertices["0"], self.vertices["3"], 4],
                ["edge0_to_2", self.vertices["0"], self.vertices["1"], 4],
                ["edge1_to_2", self.vertices["1"], self.vertices["3"], 4],
                ["edge1_to_3", self.vertices["3"], self.vertices["2"], 4],
                ["edge2_to_3", self.vertices["3"], self.vertices["4"], 4],
                ["edge0_to_3", self.vertices["4"], self.vertices["2"], 4],
            ]
        )

        graph = Graph(self.vertices.values(), self.edges.values())
        self.add(graph)

    def add_edges(self, lst):
        for id, start_vertex, end_vertex, max_capacity in lst:
            self.edges[id] = Edge(id, start_vertex, end_vertex, max_capacity)

    def add_vertices(self, lst):
        for id, x_coord, y_coord, cap in lst:
            self.vertices[id] = Vertex(id, x_coord, y_coord, cap)
