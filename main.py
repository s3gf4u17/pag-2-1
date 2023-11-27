import os

from algorithms.a_star import a_star
from algorithms.dijkstra import dijkstra
from classes.edge import Edge
from classes.graph import Graph
from classes.node import Node
from shp_utilites import elements_from_shp, create_result_shp
from txt_utilities import elements_from_txt

if __name__ == '__main__':
    graph_test = Graph()

    # For data from .txt file (up to 10 nodes)              - PASSED
    # nodes_path = os.path.abspath("database/nodes_test")
    # edges_path = os.path.abspath("database/edges_test")
    # nodes, edges = elements_from_txt(nodes_path, edges_path)
    # start_node = 0
    # end_node = 5


    # For data from small .shp file (up to 50 nodes)        - PASSED
    # shp_path = os.path.abspath("database/geodata/graph_part.shp")
    # nodes, edges, edges_geometry = elements_from_shp(shp_path)
    # start_node = 22
    # end_node = 19

    # For data from medium .shp file (up to 1000 nodes)      - :^)
    shp_path = os.path.abspath("database/geodata/graph_medium_part.shp")
    nodes, edges, edges_geometry = elements_from_shp(shp_path)
    start_node = 0
    end_node = 212

    # For data from big .shp file (up to 10 000 nodes)       - :^)
    # shp_path = os.path.abspath("database/geodata/graph_all.shp")
    # nodes, edges, edges_geometry = elements_from_shp(shp_path)
    # start_node = 8860
    # end_node = 8700

    for node in nodes:
        Node(graph_test, float(node[0]), float(node[1]))

    for edge in edges:
        Edge(graph_test, int(edge[0]), int(edge[1]), float(edge[2]))

    for edge in graph_test.edges:
        print(edge)

    #path_d = dijkstra(start_node, end_node, graph_test)
    path_a = a_star(start_node, end_node, graph_test)

    # Creating .shp files with merged path
    # create_merged_result_shp(edges_geometry, path_a).to_file(f"database/geodata/path_geo_{start_node}_{end_node}.shp")
    # create_merged_result_shp(edges_geometry, path_a).to_file(f"database/geodata/path_big_{start_node}_{end_node}.shp")

    # Creating .shp files with path consisting of separate linestring
    # create_result_shp(edges_geometry, path_a).to_file(f"database/geodata/path_geo_{start_node}_{end_node}.shp")
    create_result_shp(edges_geometry, path_a).to_file(f"database/geodata/path_medium_{start_node}_{end_node}.shp")
    # create_result_shp(edges_geometry, path_a).to_file(f"database/geodata/path_big_{start_node}_{end_node}.shp")


    #Printing list of edge's id which make path and its cost
    # print(f"Dijikstra: shortest path from node {start_node} to node {end_node} = {path_d} with cost {graph_test.nodes[end_node].g}")
    # print(f"A*:        shortest path from node {start_node} to node {end_node} = {path_a} with cost {graph_test.nodes[end_node].g}")