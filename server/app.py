from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json,csv,math

nodes = []
with open("../model/rnodes",newline="\n") as csvfile:
    nodesreader = csv.reader(csvfile,delimiter=",",quoting=csv.QUOTE_NONNUMERIC)
    for row in nodesreader: nodes.append(row)

class RequestBody(BaseModel):
    lat0:float
    lon0:float
    lat1:float
    lon1:float

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/test_line/")
async def post_line(rb:RequestBody):
    return {"type":"FeatureCollection","features":[
        {"type":"Feature","geometry":{"type":"LineString","coordinates":[[rb.lon0,rb.lat0],[rb.lon1,rb.lat1]]}}
    ]}

@app.post("/test_point/")
async def post_point(rb:RequestBody):
    mindiff0=180
    mindiff1=180
    closest0=0
    closest1=0
    for node in nodes:
        newdiff0=math.sqrt(pow(node[1]-rb.lon0,2)+pow(node[2]-rb.lat0,2))
        newdiff1=math.sqrt(pow(node[1]-rb.lon1,2)+pow(node[2]-rb.lat1,2))
        if newdiff0<mindiff0:
            mindiff0=newdiff0
            closest0=node[0]
        if newdiff1<mindiff1:
            mindiff1=newdiff1
            closest1=node[0]
    return {"type":"FeatureCollection","features":[
        {"type":"Feature","geometry":{"type":"Point","coordinates":[nodes[int(closest0)][1],nodes[int(closest0)][2]]}},
        {"type":"Feature","geometry":{"type":"Point","coordinates":[nodes[int(closest1)][1],nodes[int(closest1)][2]]}}
    ]}

@app.post("/find_path/")
async def post_path(rb:RequestBody):
    return ''