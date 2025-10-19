import api
from library import *


try:
    nSalir=1
    while nSalir==1:
        nMenu=int(input("*****MENU**********\n"
                        "1.Bulbasaur evolution chain\n"
                        "0.Exit \n"
                        ": "))
        if nMenu==1:
            URL="https://pokeapi.co/api/v2/evolution-chain/1/"
            result=api.GetData(URL)
            ListPokemon = GetPokemonList(result)
            print(f"list of pokemon evolutions: {ListPokemon}")

            objetivo = input("Enter the name you want to search for: ").lower()
            position = BinarySearch(ListPokemon, objetivo, 0, len(ListPokemon) - 1)

            if position != -1:
                print(f"el Pokemon {objetivo} se encuentra en la lista")
            else:
                print(f"Pokemon {objetivo} no encontrado.")


        elif nMenu==0:
            print("SALIR DEL PROGRAMA ")
            nSalir=0
        
        else:
             print("You chose an incorrect option- ")
except:
    print("You chose an incorrect option ")
else:
    print("")
  


