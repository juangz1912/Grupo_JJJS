def difAbsoluta(A, B):
    A.sort()
    B.sort()
    resultado = 0
    for i in range(len(A)):
        resultado += abs(A[i] - B[i])
    return resultado

lista1 = [4, 1, 8, 7]
lista2 = [2, 3, 6, 5]

print(difAbsoluta(lista1, lista2))