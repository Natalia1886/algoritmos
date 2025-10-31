from library import BuildGraphFromAPI, ShowRoute

try:
    CityOrigin = input("City of origin: ")
    CityDestination = input("City of destination: ")
    NumTravelStops = int(input("How many travel stops do you want: "))

    TravelStops = []
    for i in range(NumTravelStops):
        TravelStop = input(f"Name of TravelStop {i+1}: ")
        TravelStops.append(TravelStop)

    places = [CityOrigin] + TravelStops + [CityDestination]

except:
    print(" You chose an incorrect option.")
else:
    nodes = BuildGraphFromAPI(places)

    if not nodes:
        print("The roads could not be built.")
    else:
        print("full route:")
        route, ToTalKm = ShowRoute(nodes[0])

        print("Lugares visitados en orden:")
        for i, place in enumerate(route):
            print(f"{i+1}. {place}")

        print(f"total stops: {len(route)-2}")
        print(f"total distance traveled: {ToTalKm:.2f} km")
