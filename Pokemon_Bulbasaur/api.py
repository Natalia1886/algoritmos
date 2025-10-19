import requests
from library import Node, BuildGraph
def GetData(URL):
    try:
        Answer=requests.get(URL)
        Data=Answer.json()
    except:
        print("ERROR AL OBTENER DATOS DE LA API")
    else:
        status=Answer.status_code
        if status <200:
            print("INFORMATIVE")
            return None
        elif status<300:
            print("SUCCESS")
            Data=Answer.json()
        elif status<400:
            print("REDIRECTION")
            return None
        elif status<500:
            print("CUSTOMER ERROR")
            return None
        elif status<600:
            print("SERVER ERROR")
            return None

        else:
            print("UNKNOWN ERROR")
            return None
  


        chain = Data["chain"]

        #print(chain)

        # Crear el nodo inicial (por ejemplo Bulbasaur)
        FirstNode = Node(chain["species"]["name"])
        BuildGraph(chain, FirstNode)   
        return FirstNode

