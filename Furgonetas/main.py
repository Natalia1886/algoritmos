from library import *

try:
    print(" Optimización de ruta de entregas\n")

    NumTravelStops = int(input("¿Cuántas paradas realizará la furgoneta? "))

    if NumTravelStops < 2:
        raise ValueError("Debe ingresar al menos 2 paradas.")

    paradas = []
    for i in range(NumTravelStops):
        parada = input(f"Nombre de la parada {i + 1}: ")
        paradas.append(parada)

except Exception as e:
    print(f"\n Ocurrió un error: {e}")

else:
    print(" Construyendo el grafo con las paradas...\n")
    nodes = BuildGraphFromAPI(paradas)

    if not nodes:
        print(" No se pudieron construir las rutas (verifica los nombres de las paradas).")
    else:
        BuildEdges(nodes)
        print(" Buscando la mejor ruta (mínima distancia)...\n")
        best_path, totalKm = EncontrarMejorRuta(nodes)

        if best_path:
            ShowRoute(best_path, totalKm)
        else:
            print(" No se pudo determinar una ruta óptima.")

