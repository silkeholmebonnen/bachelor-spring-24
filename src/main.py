from manim import *
from src.DFS import DFS
from src.ford_fulkerson import FordFulkerson
from src.flow_network import FlowNetwork
from src.vertices_examples import VerticesExamples as V
from src.utils import *


class SedgewickWayne(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.sedgewick_wayne()
        layers = [1, 2, 2, 1]

        graph = FlowNetwork(
            vertices,
            edges,
            capacities,
            scene=self,
            layout="partite",
            layers=layers,
            growth_scale=GrowthScale.LINEAR,
            source=source,
            sink=sink,
            theme=Themes.Dark,
        )

        self.add(graph)
        ford_fulkerson = FordFulkerson(graph, self, show_text=False)
        ford_fulkerson.find_max_flow()


class ThoresExampleDFS(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.kleinberg_tardos_x_thore()
        layers = [1, 2, 1]
        scale = 4

        graph = FlowNetwork(
            vertices,
            edges,
            capacities,
            layout="partite",
            layers=layers,
            growth_scale=GrowthScale.LINEAR,
            source=source,
            sink=sink,
            layout_scale=scale,
            scene=self,
            theme=Themes.Dark,
        )

        self.camera.frame_width = 3.5 * scale
        self.camera.resize_frame_shape(0)
        self.add(graph)
        ford_fulkerson = FordFulkerson(graph, self, scale, path_finder=DFS())
        ford_fulkerson.find_max_flow()


class ThoresExampleBFS(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.kleinberg_tardos_x_thore()
        layers = [1, 2, 1]
        scale = 4

        graph = FlowNetwork(
            vertices,
            edges,
            capacities,
            layout="partite",
            layers=layers,
            growth_scale=GrowthScale.LINEAR,
            source=source,
            sink=sink,
            layout_scale=scale,
            scene=self,
            theme=Themes.Dark,
        )

        self.camera.frame_width = 3.5 * scale
        self.camera.resize_frame_shape(0)
        self.add(graph)
        ford_fulkerson = FordFulkerson(graph, self, scale=scale, show_text=False)
        ford_fulkerson.find_max_flow()


class BigGraph(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.silkes_big_graph()
        lt = {
            1: [-5, 0, 0],
            2: [-3, 2, 0],
            3: [-3, 0, 0],
            4: [-3, -2, 0],
            5: [-1, 3, 0],
            6: [-1, 1, 0],
            7: [-1, -1, 0],
            8: [-1, -3, 0],
            9: [1, 3, 0],
            10: [1, 1, 0],
            11: [1, -1, 0],
            12: [1, -3, 0],
            13: [3, 2, 0],
            14: [3, 0, 0],
            15: [3, -2, 0],
            16: [5, 0, 0],
        }
        scale = 5

        graph = FlowNetwork(
            vertices,
            edges,
            capacities,
            layout=lt,
            growth_scale=GrowthScale.LINEAR,
            source=source,
            sink=sink,
            layout_scale=scale,
            scene=self,
            theme=Themes.Dark,
        )

        self.camera.frame_width = scale * 3.5
        self.camera.resize_frame_shape(0)
        self.add(graph)

        ford_fulkerson = FordFulkerson(graph, self, scale, show_text=False)
        ford_fulkerson.find_max_flow()


class SimpleGraph(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.simple_graph()

        graph = FlowNetwork(
            vertices,
            edges,
            capacities,
            growth_scale=GrowthScale.LINEAR,
            source=source,
            sink=sink,
            scene=self,
            theme=Themes.Dark,
        )

        self.add(graph)
        ford_fulkerson = FordFulkerson(graph, self)
        ford_fulkerson.find_max_flow()


class WikiExample(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.wiki_example()
        layers = [1, 5, 5, 3, 1]
        scale = 3

        graph = FlowNetwork(
            vertices,
            edges,
            capacities,
            layout="partite",
            layers=layers,
            growth_scale=GrowthScale.LINEAR,
            source=source,
            sink=sink,
            layout_scale=scale,
            scene=self,
            theme=Themes.Dark,
        )

        self.camera.frame_width = 4.5 * scale
        self.camera.resize_frame_shape(0)
        self.add(graph)

        ford_fulkerson = FordFulkerson(graph, self, scale)
        ford_fulkerson.find_max_flow()
