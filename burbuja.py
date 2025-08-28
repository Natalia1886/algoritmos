def bubble_numeros(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):

            numeros_j=int(lista[j][:-1])
            numeros_1=int(lista[j+1][:-1])
            if numeros_j > numeros_1:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def bubble_letras(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            numeros_j=lista[j][-1:]
            numeros_1=lista[j+1][-1:]
            if numeros_j > numeros_1:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


lista=["2P","1D","2D","3T","5P","10T","9P","4D","8T","5D","6D","7D","3C",
       "8D","9D","11P","10D","11D","13P","1C","6T","1T","5C","3P","6C",
       "7C","11T","8C","9C","10C","11C","13C","2T","7P","8P","5T","10P",
       "12D","7T","9T","3D","12T","2C","13T","4T","1P","4P","12C","13D",
       "6P","12P","4C"]

#print(f"Lista original: {lista}")
print("******************************************************************")

lista_Num = bubble_numeros(lista)
print(f"Lista ordenada con NUMEROS: {lista_Num}")

print("******************************************************************")
lista_letras = bubble_letras(lista)
print(f"Lista ordenada con letras: {lista_letras}")


