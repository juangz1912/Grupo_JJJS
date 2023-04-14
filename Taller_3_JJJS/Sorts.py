class Sort:
    def __init__(self):
        pass

    def Merge(lista_i, lista_d):
        lista_resultado = []

        while(len(lista_i) > 0 and len(lista_d) > 0):
            if lista_i[0] < lista_d[0]:
                lista_resultado.append(lista_i[0])
                lista_i = lista_i[1:]
            else:
                lista_resultado.append(lista_d[0])
                lista_d = lista_d[1:]

        if len(lista_i) > 0:
            lista_resultado = lista_resultado + lista_i

        if len(lista_d) > 0:
            lista_resultado = lista_resultado + lista_d

        return lista_resultado

    def MergeSort(lista):
        if len(lista) <= 1:
            return lista

        lista_izquierda = lista[:len(lista)//2]  
        lista_derecha = lista[len(lista)//2:]

        lista_izquierda = self.MergeSort(lista_izquierda)
        lista_derecha = self.MergeSort(lista_derecha)

        return self.Merge(lista_izquierda, lista_derecha)