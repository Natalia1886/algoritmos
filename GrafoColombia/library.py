import math
from api import GetData  

class Node:
    def __init__(self, value):
        self.value = value
        self.connections = []
        self.lat = None
        self.lon = None

class cl_Edge:
    def __init__(self, Origin, Destination, distance_km=0):
        self.Origin = Origin
        self.Destination = Destination
        self.distance_km = distance_km

def calc_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Radio de la Tierra en km
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    return R * c

def Routes(origin_node, dest_node):
    if origin_node.lat is not None and dest_node.lat is not None:
        dist = calc_distance(origin_node.lat, origin_node.lon, dest_node.lat, dest_node.lon)
    else:
        dist = 0
    edge = cl_Edge(origin_node, dest_node, dist)
    origin_node.connections.append(edge)

# Construir el grafo con los Places dados
def BuildGraphFromAPI(Places):
    nodos = []
    for Place in Places:
        info = GetData(Place)
        if info:
            nodo = Node(Place)
            nodo.lat = float(info["lat"])
            nodo.lon = float(info["lon"])
            nodos.append(nodo)
        else:
            print(f"No se pudo obtener información para {Place}")

    for i in range(len(nodos) - 1):
        Routes(nodos[i], nodos[i + 1])
    return nodos

def ShowRoute(node, visited=None, result=None, total_distance=0):
    if visited is None:
        visited = set()
    if result is None:
        result = []
    if node.value in visited:
        return result, total_distance

    visited.add(node.value)
    result.append(node.value)

    for edge in node.connections:
        print(f"{edge.Origin.value} → {edge.Destination.value}: {edge.distance_km:.2f} km")
        total_distance += edge.distance_km
        result, total_distance = ShowRoute(edge.Destination, visited, result, total_distance)

    return result, total_distance
