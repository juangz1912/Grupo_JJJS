# Definir la matriz
matriz = [[1, 2, 3],[5, 6, 7],[9, 10, 11],[13, 14, 15], [17, 18, 19], [21, 22, 23]] #O(1)
# Definir las dimensiones de la matriz
filas = len(matriz)  #O(1)
columnas = len(matriz[0])#O(1)
# Recorrer la matriz en zigzag de arriba a abajo
for j in range(columnas): #O(n)
    if j % 2 == 0:#O(n)
        # Recorrer de arriba a abajo en las columnas pares
        for i in range(filas):#O(n)(n)
            print(matriz[i][j], end=' ')#O(n)(n)
    else:#O(n)
        # Recorrer de abajo a arriba en las columnas impares
        for i in range(filas-1, -1, -1):#O(n)(n)
            print(matriz[i][j], end=' ')#O(n)(n)
#3(1)+3(n)+4(n^2)
#O(n^2)
