from algorithms.dijkstra import dijkstra
from classes.edge import Edge
from classes.graph import Graph
from classes.node import Node

if __name__ == '__main__':
    graph_test = Graph()

    Nodes = [Node(graph_test, 0, 0),
             Node(graph_test, 1, 0),
             Node(graph_test, 0, 1),
             Node(graph_test, 1, 1),
             Node(graph_test, 2, 1),
             Node(graph_test, 2, 0)]

    edges = [Edge(graph_test, 0, 1, 1),
             Edge(graph_test, 0, 2, 2),
             Edge(graph_test, 1, 0, 1),
             Edge(graph_test, 1, 3, 2),
             Edge(graph_test, 2, 0, 2),
             Edge(graph_test, 2, 3, 2),
             Edge(graph_test, 2, 5, 6),
             Edge(graph_test, 3, 1, 2),
             Edge(graph_test, 3, 2, 2),
             Edge(graph_test, 3, 4, 2),
             Edge(graph_test, 3, 4, 2),
             Edge(graph_test, 4, 3, 2),
             Edge(graph_test, 4, 5, 2),
             Edge(graph_test, 5, 2, 6),
             Edge(graph_test, 5, 4, 2)]

    print(f"Shortest path to node 5 = {dijkstra(0, 5, graph_test)} with cost {graph_test.nodes[5].g}")
