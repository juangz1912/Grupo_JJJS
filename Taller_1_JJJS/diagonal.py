matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  #O(1)
# inicializa la variable de dirección como 1 para moverse hacia la derecha
direccion = 1 #O(1)
# inicializa el índice de fila y columna
fila = 0 #O(1)
columna = 0 #O(1)

# recorre la matriz en zigzag
for i in range(len(matriz) * len(matriz[0])): #O(n)
    print(matriz[fila][columna]) #O(n)

    # cambia la dirección si la fila es cero o la última
    if fila == 0 or fila == len(matriz) - 1: #O(n)
        direccion *= -1 #O(n)

    # actualiza la fila y columna según la dirección
    if direccion == 1: #O(n)
        fila += 1#O(n)
    else: #O(n)
        fila -= 1 #O(n)
        columna += 1 #O(n) 


#4(1)+9(n)