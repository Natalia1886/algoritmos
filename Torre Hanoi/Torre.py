def torre_hanoi(nDiscos):
    nMovimientos = ((2**(nDiscos)) - 1)
    Palo1 = []
    Palo2 = []
    Palo3 = []

    # Crear la torre inicial en Palo1
    for i in range(nDiscos, 0,-1):
        Palo1.append(i)

    print("Estado inicial: \n",        f"Palo1:, {Palo1} \n",
        f"Palo2:, {Palo2} \n",
        f"Palo3:, {Palo3} \n",
        "************************")

  

    # Simulación de movimientos sin recursividad
    for i in range(0, nMovimientos +1):
        if i % 3 == 1:
            # Mover entre origen y destino
            mover(Palo1, Palo3)
        elif i % 3 == 2:
            # Mover entre origen y auxiliar
            mover(Palo1, Palo2)
        elif i % 3 == 0:
            # Mover entre auxiliar y destino
            mover(Palo2, Palo3)


        print(f"Movimiento {i}: \n",
                f"Palo1:, {Palo1} \n",
                f"Palo2:, {Palo2} \n",
                f"Palo3:, {Palo3} \n",
                "************************")

        

    print("Estado final:", Palo1, Palo2, Palo3)
    return nMovimientos


def mover(origen, destino):
    if not origen and not destino:
        return


    if not origen:
        origen.append(destino[-1])
        del destino[-1]
    elif not destino:
        destino.append(origen[-1])
        del origen[-1]
    elif origen[-1] < destino[-1]:
        destino.append(origen[-1])
        del origen[-1]
    else:
        origen.append(destino[-1])
        del destino[-1]


try:
    nDiscos = int(input("Digite numero de discos: "))
except:
    print("Digite un numero valido")
else:
    ToTalCombinaciones = torre_hanoi(nDiscos)
    if ToTalCombinaciones != -1:
        print("Numero de combinaciones usadas: ", ToTalCombinaciones)
    else:
        print("ERROR")
