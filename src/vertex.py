from manim import *


class Vertex(Dot):
    def __init__(self, id, x_coord, y_coord, max_capacity, **kwargs):
        self.id = id
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.max_capacity = max_capacity
        self.opacity = 0
        self.current_flow = 0

        super().__init__(point=self.to_np_array(), color=BLACK, z_index=0, **kwargs)
        # super().scale(max_capacity + 0.2)

    def draw(self):
        foregroundDot = (
            Dot(self.to_np_array())
            .scale(self.max_capacity)
            .set_fill(WHITE)
            .set_z_index(10)
        )

        self.add(foregroundDot)

        backgroundDot = (
            Dot(self.to_np_array())
            .scale(self.max_capacity + 0.2)
            .set_fill(BLACK)
            .set_z_index(0)
        )

        self.add(backgroundDot)

        label = Tex(self.id, color=BLACK).set_x(self.x_coord).set_y(self.y_coord)
        label.set_z_index(20).scale(0.8)
        self.add(label)

    def to_np_array(self):
        return np.array([self.x_coord, self.y_coord, 0])

    def add_to_max_capacity(self, capacity):
        if self.max_capacity < capacity:
            self.max_capacity = capacity

    def add_to_opacity(self, amount):
        self.opacity += amount

    def get_opacity(self, flow):
        return flow / self.opacity

    def get_max_capacity(self):
        return self.max_capacity

    def add_to_current_flow(self, new_flow):
        if new_flow <= self.max_capacity:
            self.current_flow += new_flow
        else:
            print("Error: New capacity exceeds maximum capacity")


"""
class Ex(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        v = Vertex("vertex0", 0, 0, 5)
        self.add(v)
        self.wait(1)

        v2 = Vertex("vertex1", 2, 2, 4)
        self.add(v2)
        self.wait(1)
 """
