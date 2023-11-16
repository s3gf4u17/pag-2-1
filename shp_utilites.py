import geopandas as gpd
import pandas as pd
from shapely.ops import unary_union

def elements_from_shp(path: str):
    shp = gpd.read_file(path)
    shp['length'] = shp.length
    shp['first_pnt'] = shp.apply(lambda x: x['geometry'].coords[0], axis=1)
    shp['last_pnt'] = shp.apply(lambda x: x['geometry'].coords[-1], axis=1)
    #shp.insert(0, 'Edge_Id', shp.index)
    shp_edges = shp[['first_pnt', 'last_pnt', 'length', 'klasaDrogi']].copy()
    edges_geometry = shp['geometry'].copy()
    edges = shp_edges.values.tolist()

    nodes = []
    for i,edge in enumerate(edges):
        start = edge[0]
        end = edge[1]
        if start not in nodes:
            nodes.append(start)
            edges[i][0] = len(nodes)-1
        else:
            edges[i][0] = nodes.index(start)

        if end not in nodes:
            nodes.append(end)
            edges[i][1] = len(nodes)-1
        else:
            edges[i][1] = nodes.index(end)

    #Example of edges list
    #[0, 1, 151.2902927968559, 'L']
    #[1, 2, 92.81779704915195, 'L']
    #[3, 4, 81.63997599812492, 'L']
    #[5, 6, 39.38142963381905, 'L']
    return edges, edges_geometry

#Yet to be tested
def create_result_shp(edges_geometry: list, path_parts: list):
    shortest_path = gpd.GeoDataFrame(columns=["geometry"],geometry="geometry", crs="EPSG:2180")
    for index in path_parts:
        part = edges_geometry[int(index)]
        unary_union([shortest_path, part])
    return shortest_path

