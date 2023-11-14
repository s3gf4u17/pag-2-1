import geopandas as gpd
import pandas as pd

def shp_mk(path: str):
    shp = gpd.read_file(path)
    shp['length'] = shp.length
    shp['first_pnt'] = shp.apply(lambda x: x['geometry'].coords[0], axis=1)
    shp['last_pnt'] = shp.apply(lambda x: x['geometry'].coords[-1], axis=1)
    shp_edges = shp[['first_pnt', 'last_pnt', 'length', 'klasaDrogi']].copy()
    linestrings = shp['geometry'].copy()
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

    return edges, linestrings