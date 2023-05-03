def MenorMultiplicacion(A, B):
    A.sort()
    B.sort(reverse=True)
    resultado = 0
    for i in range(len(A)):
        resultado += A[i] * B[i]
    return resultado

lista1 = [6, 1, 9, 5, 4]
lista2 = [3, 4, 8, 2, 4]

print(MenorMultiplicacion(lista1, lista2))