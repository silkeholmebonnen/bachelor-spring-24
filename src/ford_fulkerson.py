from src.BFS import BFS
from manim import *
from src.flow_network import FlowNetwork
from src.text_helper import TextHelper
from src.flow import Flow


class FordFulkerson:
    def __init__(
        self,
        graph: FlowNetwork,
        scene: Scene,
        scale=2,
        show_text=True,  # Set to false to disable LaTex animations
        path_finder=BFS(),
    ):
        self.graph = graph
        self.scene = scene
        self.max_flow = 0
        self.text_helper = TextHelper(graph, scene, scale, show_text=show_text)
        self.path_finder = path_finder

    def find_max_flow(self):
        self.max_flow = 0

        self.text_helper.play_initial_tex_animation()

        path = self.path_finder.find_path(
            source=self.graph.source,
            sink=self.graph.sink,
            graph_length=len(self.graph.vertices),
        )
        while path:
            self.max_flow += self.augment_path(path)
            path = self.path_finder.find_path(
                source=self.graph.source,
                sink=self.graph.sink,
                graph_length=len(self.graph.vertices),
            )

        self.text_helper.play_final_tex_animation(int(self.max_flow))

    def augment_path(self, path):
        bottleneck = 9223372036854775807
        current_vertex = self.graph.sink
        path_to_draw = []

        while current_vertex.id is not self.graph.source.id:
            bottleneck = min(
                bottleneck,
                path.get(current_vertex.id).get_residual_capacity_to(current_vertex),
            )
            current_vertex = path.get(current_vertex.id).get_other_vertex(
                current_vertex
            )

        current_vertex = self.graph.sink

        while current_vertex.id is not self.graph.source.id:
            path_to_draw.insert(
                0, (current_vertex.id, path.get(current_vertex.id))
            )  # insert the edge in the beginning of the list
            current_vertex = path.get(current_vertex.id).get_other_vertex(
                current_vertex
            )

        self.text_helper.play_tex_animation_for_residual_graph_before()

        # disable to hide the animation of playing the residual graph
        self.graph.show_residual_graph(self.scene, path_to_draw, self.text_helper)

        self.text_helper.play_tex_animation_for_path(path_to_draw, bottleneck)

        for vertex, edge in path_to_draw:
            edge.add_current_flow_towards(vertex, bottleneck, self.scene)

        self.display_flow_path_helper(path_to_draw, bottleneck)

        return bottleneck

    """ Helper method to displays the flow VMobjects on the path from s to t """

    def display_flow_path_helper(self, path_to_draw, bottleneck):
        corner_arr = []
        corner_arr.append(self.graph.source.to_np_array())

        for vertex, edge in path_to_draw:
            corner_arr.append(edge.get_vertex_from_id(vertex).to_np_array())

        path = VMobject()
        path.set_points_as_corners(corner_arr)

        # The way this is currently done, you cannot undo a flow. You would need to save this flow to undo it later.
        Flow(
            path,
            scene=self.scene,
            kilter_start=-(bottleneck * 8 / 200),
            kilter_end=(bottleneck * 8 / 200),
            theme=self.graph.theme,
        )
