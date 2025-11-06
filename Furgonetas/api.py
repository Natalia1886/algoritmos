import requests

# Función para obtener coordenadas de un lugar usando Nominatim (OpenStreetMap)
def GetData(NamePlace):
    URL = f"https://nominatim.openstreetmap.org/search?format=json&q={NamePlace}"
    try:
        respuesta = requests.get(URL, headers={'User-Agent': 'RouteFinderApp'})
        data = respuesta.json()
    except Exception as e:
        print("ERROR AL OBTENER DATOS DE LA API:", e)
        return None
    else:
        status = respuesta.status_code
        if status >= 200 and status < 300:
            if len(data) == 0:
                print(f" No data was found data {NamePlace}")
                return None
            else:
                print(f"SUCCESFULL")
                return data[0]  # 
        else:
            print(f"Error  ({status})")
            return None
