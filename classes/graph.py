from classes.edge import Edge, Node

class Graph:
    def __init__(self, nodes: list[Node], edges: list[Edge]):
        self.nodes = nodes
        self.edges = edges