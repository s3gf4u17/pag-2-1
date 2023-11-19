class Node:
    def __init__(self, id: str, x: float, y: float, f: float = 0, g: float = 0, neighbours: list["Edge"] = None):
        self.id = id
        self.x = x
        self.y = y
        self.f = f
        self.g = g
        self.neighbours = neighbours