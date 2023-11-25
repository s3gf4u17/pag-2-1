from classes.graph import Graph


class Node:
    def __init__(self, graph: Graph, x: float, y: float, neighbors: list[int] = None, f: float = float('inf'),
                 g: float = float('inf'), id: int = 0):
        self.id = len(graph.nodes)
        self.x = x
        self.y = y
        self.f = f
        self.g = g
        self.neighbors = []
        graph.nodes.append(self)

    def add_neighbor(self, new_neighbor):
        self.neighbors.append(new_neighbor)
