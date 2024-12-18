from manim import *

from src.edge import Edge
from src.vertex import Vertex


class Test_Edge(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        vertex0 = Vertex("0", 0, 0)
        vertex1 = Vertex("1", 1, 0)
        edge = Edge(vertex0, vertex1, 5, self)

        vertex0.draw()
        vertex1.draw()
        edge.draw()

        self.add(edge)
        self.add(vertex0)
        self.add(vertex1)
