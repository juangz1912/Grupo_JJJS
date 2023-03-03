def recorrer_zigzag(matriz, fila, columna, direccion):
    # caso base: si la fila es igual a la longitud de la matriz, se ha recorrido toda la matriz
    if fila == len(matriz):
        return
    # imprimir el valor actual y llamar recursivamente a la función en la siguiente celda
    print(matriz[fila][columna])
    if direccion == 1:
        if columna == len(matriz[0]) - 1:
            recorrer_zigzag(matriz, fila + 1, columna, -1)
        elif fila == 0:
            recorrer_zigzag(matriz, fila, columna + 1, -1)
        else:
            recorrer_zigzag(matriz, fila - 1, columna + 1, 1)
    else:
        if fila == len(matriz) - 1:
            recorrer_zigzag(matriz, fila, columna + 1, 1)
        elif columna == 0:
            recorrer_zigzag(matriz, fila + 1, columna, 1)
        elif fila < len(matriz) - 1 and columna > 0:
            recorrer_zigzag(matriz, fila + 1, columna - 1, -1)

# ejemplo de uso
matriz = [[1, 2, 3, 4], 
          [5, 6, 7, 8], 
          [9, 10, 11, 12], 
          [13, 14, 15, 16]]
recorrer_zigzag(matriz, 0, 0, 1)


