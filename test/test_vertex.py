from manim import *
from src.vertex import Vertex


class Test_Vertex(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        vertex = Vertex("0", 0, 0, 5)

        vertex.draw()

        self.add(vertex)
