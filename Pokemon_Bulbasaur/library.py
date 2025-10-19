class Node:
    def __init__(self, value):
        self.value = value
        self.connections = []

class cl_Edge:
    def __init__(self, Origin, Destination):
        self.Origin = Origin
        self.Destination = Destination

#BUILD THE GRAPH
def BuildGraph( chain,StartNode=None, Visited=None):
    name = chain["species"]["name"]

    if Visited is None:
        Visited = set()
    
    if StartNode in Visited:
        return
    
    if StartNode is None:
        StartNode = Node(name)
        print(f"Nodo: {StartNode.value}")
    
    Visited.add(name)
    print(f"Nodo: {StartNode.value}")
    
    for Change in chain["evolves_to"]:
        ChangeName = Change["species"]["name"]
        # Crear el nodo de destino
        NextNode = Node(ChangeName)
        # Conectarlo al nodo actual
        edge = cl_Edge(StartNode, NextNode)
        StartNode.connections.append(edge)
    
        BuildGraph(Change, NextNode, Visited)
    return StartNode
def route(node, visited, result):
    if node.value in visited:
        return
    visited.add(node.value)
    result.append(node.value)
    for edge in node.connections:
        route(edge.Destination, visited, result)


def route(node, visited, result):
    if node.value in visited:
        return
    visited.add(node.value)
    result.append(node.value)
    for edge in node.connections:
        route(edge.Destination, visited, result)


def GetPokemonList(StartNode):
    if StartNode is None:
        return []
    visited = set()
    result = []
    route(StartNode, visited, result)
    return result

def organizar_diccionario(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list



def BinarySearch(arr, start, low, high):
    if low > high:
        return -1
    middle = (low + high) // 2

    if arr[middle] == start:
        return middle
    elif arr[middle] < start:
        return BinarySearch(arr, start, middle + 1, high)
    else:
        return BinarySearch(arr, start, low, middle - 1)

