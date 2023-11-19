import heapq
from classes.node import Node

class PriorityQueue:
    def __init__(self):
        self.elements: list[tuple[float, Node]] = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item: Node, priority: float):
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> Node:
        return heapq.heappop(self.elements)[1]