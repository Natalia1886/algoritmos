import requests


def busqueda_lineal(diccionario, objetivo):       
        for i in diccionario:
            if i["name"]["common"]==objetivo:
                return i["maps"]["googleMaps"]
        return -1

def busqueda_binaria(diccionario,objetivo):
    bajo, alto = 0, len(diccionario) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if diccionario[medio]["name"]["common"] == objetivo:
            return diccionario[medio]["maps"]["googleMaps"]
        elif diccionario[medio]["name"]["common"] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1
# TAREA

def organizar_diccionario(diccionario):
    n=len(diccionario)
    for i in range (n):
         for j in range (0, n-i-1):
              if diccionario[j]["name"]["common"]>diccionario[j+1]["name"]["common"]:
                   diccionario[j],diccionario[j+1]=diccionario[j+1] , diccionario[j] 
    return diccionario 
     

URL="https://restcountries.com/v3.1/region/europe"

respuesta=requests.get(URL)
datos=respuesta.json()
print(respuesta)
#print(datos)
nombre_pais=input("PAÍS: ")
nTipoBusqueda=int(input("Seleccione que tipo de busqueda desea usar \n"
                       "1.Busqueda lineal \n"
                       "2.Busqueda binaria \n"
                       ":  "))
if nTipoBusqueda==1:
    print("********BUSQUEDA LINEAL***********")
    paisLineal=busqueda_lineal (datos, nombre_pais)
    if paisLineal != -1:
        print(f"El PAÍS: {nombre_pais} \n"
            f"Ubicación: {paisLineal} \n")
    else:
        print(f"{nombre_pais} no se encuentra en la API.")


elif nTipoBusqueda==2:
    print("***********BUSQUEDA BINARIA***********")
    D_Organizado=organizar_diccionario(datos)
    paisBinario=busqueda_binaria(D_Organizado,nombre_pais)
    if paisBinario != -1:
        print(f"PAÍS: {nombre_pais} \n"
               f"Ubicacion:{paisBinario} ")

    else:
        print(f"{nombre_pais} no se encuentra en la API.")


                
