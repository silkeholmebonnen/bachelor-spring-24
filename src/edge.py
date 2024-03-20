from manim import *
from src.arrow import EdgeArrow


class Edge(VMobject):
    def __init__(self, start_vertex, end_vertex, max_capacity, current_flow=0):
        super().__init__()

        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.max_capacity = max_capacity
        self.current_flow = current_flow

        start_vertex.add_to_max_capacity(max_capacity)
        end_vertex.add_to_max_capacity(max_capacity)

        # also add to opacity
        # start_vertex.add_to_opacity(max_capacity)
        # end_vertex.add_to_opacity(max_capacity)

    def add_to_current_flow(self, new_flow):
        if new_flow <= self.max_capacity:
            self.current_flow += new_flow
        else:
            print("Error: New capacity exceeds maximum capacity")

    def draw(self):
        backgroundLine = Line(
            start=self.start_vertex.to_np_array(),
            end=self.end_vertex.to_np_array(),
            z_index=0,
            color=BLACK,
            stroke_width=((self.max_capacity + 0.2) * 16),
        )
        foregroundLine = (
            Line(
                start=self.start_vertex.to_np_array(),
                end=self.end_vertex.to_np_array(),
                z_index=3,
            )
            .set_stroke(width=(self.max_capacity * 16), color=WHITE)
            .set_fill(color=WHITE)
        )
        arrow = EdgeArrow(
            self.start_vertex.to_np_array(), self.end_vertex.to_np_array()
        )

        self.add(backgroundLine)
        self.add(foregroundLine)
        self.add(arrow)


"""
class Ex(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        v1 = Vertex("vertex0", -4, 0, 5)

        v2 = Vertex("vertex1", 4, 2, 4)
        e = Edge("vertex0", v1, v2, 4)
        self.add(v1)
        self.add(v2)
        self.add(e)
        self.wait(1)
 """
