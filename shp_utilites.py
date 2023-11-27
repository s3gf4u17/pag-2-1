import geopandas as gpd
from shapely.ops import linemerge

from classes.graph import Graph


def road_class_to_weight(rclass: str) -> float:
    speed_limit: float = 140

    if rclass == "A" or rclass == "I":  # autostrada lub inna
        speed_limit = 140
    elif rclass == "S":  # ekspresowa
        speed_limit = 130
    elif rclass == "GP":  # główna ruchu przyspieszonego
        speed_limit = 110
    elif rclass == "G":  # główna
        speed_limit = 100
    elif rclass == "Z":  # zbiorcza
        speed_limit = 80
    elif rclass == "L":  # lokalna
        speed_limit = 60
    elif rclass == "D":  # zbiorcza
        speed_limit = 30

    return speed_limit


def elements_from_shp(path: str):
    shp = gpd.read_file(path)
    shp = shp.set_crs("EPSG:2180")
    shp['length'] = shp.length
    shp["speed_limit"] = shp['klasaDrogi'].apply(road_class_to_weight)
    shp['first_pnt'] = shp.apply(lambda x: x['geometry'].coords[0], axis=1)
    shp['last_pnt'] = shp.apply(lambda x: x['geometry'].coords[-1], axis=1)
    shp_edges = shp[['first_pnt', 'last_pnt', 'length', 'speed_limit']].copy()
    edges_geometry = shp['geometry'].copy()
    edges = shp_edges.values.tolist()

    nodes = []
    for i, edge in enumerate(edges):
        start = edge[0]
        end = edge[1]
        if start not in nodes:
            nodes.append(start)
            edges[i][0] = len(nodes) - 1
        else:
            edges[i][0] = nodes.index(start)

        if end not in nodes:
            nodes.append(end)
            edges[i][1] = len(nodes) - 1
        else:
            edges[i][1] = nodes.index(end)

    return nodes, edges, edges_geometry


def create_result_shp(edges_geometry: list, path_parts: list):
    path = []
    for winning_edge in path_parts:
        path.append(edges_geometry[winning_edge])

    # path_geo = linemerge(path)
    shortest_path = gpd.GeoDataFrame(geometry=path, crs="EPSG:2180")
    return shortest_path

def create_merged_result_shp(edges_geometry: list, path_parts: list):
    path = []
    for winning_edge in path_parts:
        path.append(edges_geometry[winning_edge])

    path_geo = linemerge(path)
    shortest_path = gpd.GeoDataFrame(geometry=[path_geo], crs="EPSG:2180")
    return shortest_path