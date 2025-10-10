# Crea una función recursiva que calcule la suma de todos los dígitos
# de un número entero positivo dado (N).

# Lógica Recursiva:
# La suma de los dígitos de N es resultado al último dígito (N(mod10))
# más la suma de los dígitos del número restante (N//10).



def suma (nNum,inicio):
    if nNum<=0:
        print ("la suma es ", inicio)
    else:

        mod=nNum%10
        nNum=nNum//10

        return suma (nNum,inicio+mod)
try:
    inicio=0
    nNum=int(input("Digite un numero: "))
except:
    print("DIGITE UN NUMERO VALIDO")
else:
    suma (nNum,inicio)
    
    
