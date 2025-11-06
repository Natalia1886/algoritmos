import math
from api import GetData  

# ------------------- Clases -------------------

class Node:
    def __init__(self, value, lat=None, lon=None):
        self.value = value
        self.lat = lat
        self.lon = lon
        self.connections = []  # aristas salientes


class Edge:
    def __init__(self, Origin, Destination, distance_km):
        self.Origin = Origin
        self.Destination = Destination
        self.distance_km = distance_km


# ------------------- Cálculos -------------------

def calc_distance(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


def calc_tiempo_viaje(distancia_km, velocidad_promedio=30):
    return (distancia_km / velocidad_promedio) * 60



def BuildGraphFromAPI(places):
    nodos = []
    for place in places:
        info = GetData(place)
        if info:
            nodo = Node(place, float(info["lat"]), float(info["lon"]))
            nodos.append(nodo)
        else:
            print(f" No se pudo obtener información para {place}.")
    return nodos


def BuildEdges(nodes):
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i != j:
                dist = calc_distance(nodes[i].lat, nodes[i].lon, nodes[j].lat, nodes[j].lon)
                edge = Edge(nodes[i], nodes[j], dist)
                nodes[i].connections.append(edge)



def EncontrarMejorRuta(nodes):
    mejor_ruta = None
    menor_distancia = float('inf')

    def buscar_ruta(actual, visitados, distancia):
        nonlocal mejor_ruta, menor_distancia

        # Si ya visitó todos los nodos, evaluamos si esta ruta es la más corta
        if len(visitados) == len(nodes):
            if distancia < menor_distancia:
                menor_distancia = distancia
                mejor_ruta = visitados[:]
            return

        for edge in actual.connections:
            if edge.Destination not in visitados:
                buscar_ruta(edge.Destination, visitados + [edge.Destination], distancia + edge.distance_km)

    # Intentamos comenzar desde cada nodo
    for start in nodes:
        buscar_ruta(start, [start], 0)

    return mejor_ruta, menor_distancia


# ------------------- Mostrar resultados -------------------

def ShowRoute(best_path, total_distance):
    """Muestra la mejor ruta encontrada."""
    print(" Ruta óptima encontrada:\n")
    for i, node in enumerate(best_path):
        print(f"{i + 1}. {node.value}")
    print(f"  Distancia total mínima: {total_distance:.2f} km")
    print(f"  Tiempo estimado: {calc_tiempo_viaje(total_distance):.2f} minutos")
