from manim import *
from src.ManimGraphLibrary import *
from src.ford_fulkerson import FordFulkerson
from src.flow_network import FlowNetwork
from src.vertices_examples import VerticesExamples as V
from src.utils import GrowthScale


class Main(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.sedgewick_wayne()

        layers = [1, 2, 2, 1]

        graph = FlowNetwork(
            vertices,
            edges,
            capacities,
            layout="partite",
            layers=layers,
            growth_scale=GrowthScale.LINEAR,
            source=source,
            sink=sink,
        )

        self.add(graph)

        ford_fulkerson = FordFulkerson(graph)
        ford_fulkerson.find_max_flow(self)

        self.wait(2)
