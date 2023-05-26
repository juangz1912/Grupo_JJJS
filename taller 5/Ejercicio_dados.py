def generar_combinaciones(valor_dado, dados, resultado_actual=[]):
    #revisa si el len de la lista es igual a la cantidad de los dados
    if len(resultado_actual) == dados:
        #verifica si la suma de todos los valores de la lista son mayor al valor dado
        if sum(resultado_actual) > valor_dado:
            print(resultado_actual)
        return
    #crea todas los combinaciones de dados 
    for i in range(1, 7):
        generar_combinaciones(valor_dado, dados, resultado_actual + [i])

valor_dado = 23
dados = 4

generar_combinaciones(valor_dado, dados)
