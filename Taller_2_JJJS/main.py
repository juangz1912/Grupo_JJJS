import Formulas as form

print("Importa el orden? \n 1. Si \n 2. No")
tipo_ejercicio = int(input())

print("Intervienen todos los elementos? \n 1. Si \n 2. No")
intervencion = int(input())

print("Se repiten elementos? \n 1. Si \n 2. No")
repeticion = int(input())

if tipo_ejercicio == 1 and intervencion == 1  and repeticion == 1:
    print("Es una permutación con repetición")

if tipo_ejercicio == 2 and intervencion == 2 and repeticion == 1:
    print("Es una combinación con repetición")

if tipo_ejercicio == 1 and intervencion == 2 and repeticion == 1:
    print("Es una variación con repetición")

if tipo_ejercicio == 1 and intervencion == 1 and repeticion == 2:
    print("Es una permutación ordinaria")

if tipo_ejercicio == 2 and intervencion == 2 and repeticion == 2:
    print("Es una combinación ordinaria")

if tipo_ejercicio == 1 and intervencion == 2 and repeticion == 2:
    print("Es una variación ordinaria")