lista = [1,2,3,4,5,6,2]

def repetidos(lista, recorridos=[], n_repetidos=[]):
    if len(lista) == 0:
        return n_repetidos
    n = lista.pop()

    if (n not in n_repetidos) and (n in recorridos):
        n_repetidos.append(n)
        return repetidos(lista, recorridos, n_repetidos)
    if n not in recorridos:
        recorridos.append(n)
        return repetidos(lista, recorridos, n_repetidos)
    

print(repetidos(lista))