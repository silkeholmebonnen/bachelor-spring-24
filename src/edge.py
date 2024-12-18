from manim import *
from src.arrow import EdgeArrow
from src.utils import *

ratefunctions = [
    rate_functions.double_smooth,
    rate_functions.linear,
    rate_functions.ease_in_sine,
    rate_functions.ease_out_quad,
    rate_functions.ease_in_quint,
    rate_functions.ease_in_cubic,
    rate_functions.ease_in_out_circ,
]

color_list = color_gradient([AS2700.B32_POWDER_BLUE, AS2700.B45_SKY_BLUE], 6)


class Edge(VMobject):
    def __init__(
        self,
        start_vertex,
        end_vertex,
        max_capacity,
        current_flow=0,
        growth_scale=GrowthScale.SQRT,
        theme=Themes.Light,
        scene: Scene = None,
    ):
        super().__init__()
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.max_capacity = max_capacity
        self.current_flow = current_flow
        self.growth_scale = growth_scale
        self.theme = theme

        start_vertex.add_adjacent_edge(self)
        end_vertex.add_adjacent_edge(self)

        if max_capacity > start_vertex.biggest_capacity:
            start_vertex.biggest_capacity = max_capacity
        if max_capacity > end_vertex.biggest_capacity:
            end_vertex.biggest_capacity = max_capacity

        self.start_vertex_to_updater = {}

    def add_current_flow_towards(self, vertex_id, new_flow, scene: Scene):
        # if vertex is start_vertex, that means we want to 'undo' a previous choice
        if vertex_id is self.start_vertex.id:
            new_flow = -1 * new_flow

        self.current_flow += new_flow

    def get_drawn_edge_size(self, capacity):
        return get_drawn_size(self.growth_scale, capacity) * 8

    def draw(self):
        background_line = Line(
            start=self.start_vertex.to_np_array(),
            end=self.end_vertex.to_np_array(),
            color=self.theme.get("BORDER"),
            stroke_width=(self.get_drawn_edge_size(self.max_capacity) + 1.6),
        )

        self.foreground_line = (
            Line(
                start=self.start_vertex.to_np_array(),
                end=self.end_vertex.to_np_array(),
            )
            .set_stroke(
                width=self.get_drawn_edge_size(self.max_capacity),
                color=self.theme.get("OBJECT-BACKGROUND"),
            )
            .set_fill(color=self.theme.get("OBJECT-BACKGROUND"))
            .set_z_index(3)
        )

        self.arrow = EdgeArrow(
            self.start_vertex.to_np_array(), self.end_vertex.to_np_array(), self.theme
        )

        self.add(background_line, self.foreground_line, self.arrow)

    def get_direction(self):
        x_start = self.start_vertex.x_coord
        y_start = self.start_vertex.y_coord
        x_end = self.end_vertex.x_coord
        y_end = self.end_vertex.y_coord
        v1 = x_end - x_start
        v2 = y_end - y_start
        edge_vector = np.array([v1, v2, 0])

        return edge_vector / np.linalg.norm(edge_vector)

    def get_new_arrow_coords(self):
        a, b = self.get_vector_values()
        height_to_new_point = self.get_drawn_edge_size(self.current_flow) / 100 / 2
        orthogonal_vector = np.array([b, -a, 0])

        return self.get_offset_points(height_to_new_point, orthogonal_vector)

    def get_flow_coords(self):
        a, b = self.get_vector_values()
        orthogonal_vector = np.array([-b, a, 0])
        half_line_width = (self.get_drawn_edge_size(self.max_capacity) / 100) / 2
        height_to_new_point = half_line_width - (
            self.get_drawn_edge_size(self.current_flow) / 100 / 2
        )

        return self.get_offset_points(height_to_new_point, orthogonal_vector)

    def get_offset_points(self, offset, orthogonal_vector):
        orthogonal_unit_vector = orthogonal_vector / np.linalg.norm(orthogonal_vector)
        scaled_orthogonal_vector = orthogonal_unit_vector * offset
        start_coord = self.start_vertex.to_np_array() + scaled_orthogonal_vector
        end_coord = self.end_vertex.to_np_array() + scaled_orthogonal_vector

        return (
            start_coord,
            end_coord,
        )

    def get_vector_values(self):
        x_start = self.start_vertex.x_coord
        y_start = self.start_vertex.y_coord
        x_end = self.end_vertex.x_coord
        y_end = self.end_vertex.y_coord

        return (x_end - x_start), (y_end - y_start)

    def get_residual_capacity_to(self, vertex):
        if vertex.id is self.end_vertex.id:
            return self.max_capacity - self.current_flow
        else:
            return self.current_flow

    def get_other_vertex(self, vertex):
        if vertex.id is self.end_vertex.id:
            return self.start_vertex
        else:
            return self.end_vertex

    def get_other_vertex_from_id(self, vertex_id):
        if vertex_id is self.end_vertex.id:
            return self.start_vertex
        else:
            return self.end_vertex

    def get_vertex_from_id(self, vertex_id):
        if vertex_id is self.end_vertex.id:
            return self.end_vertex
        else:
            return self.start_vertex

    def get_active_edges(self):
        active_edges = []
        if self.current_flow > 0:
            active_edges.append((self.end_vertex.id, self.start_vertex.id))
        if self.current_flow < self.max_capacity:
            active_edges.append((self.start_vertex.id, self.end_vertex.id))
        return active_edges
