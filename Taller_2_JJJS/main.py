print("Importa el orden? \n 1. Si \n 2. No")
tipo_ejercicio = input()

print("Se repiten elementos? \n 1. Si \n 2. No")
repeticion = input()

if tipo_ejercicio == 1 and repeticion == 1:
    print("Es una permutación")

if tipo_ejercicio == 2 and repeticion == 1:
    print("Es una combinación y se repiten elementos")

if tipo_ejercicio == 1 and repeticion == 2:
    print("Es una permutación")

if tipo_ejercicio == 2 and repeticion == 2:
    print("Es una combinación y no se repiten elementos")