import Formulas

def mostrar_menu():
    print("1. Variaciones ordinarias")
    print("2. Variaciones con repetición")
    print("3. Permutaciones ordinarias")
    print("4. Permutaciones con repetición")
    print("5. Combinaciones ordinarias")
    print("6. Combinaciones con repetición")

def obtener_formula():
    tipo = int(input("Ingrese el tipo de técnica de conteo (1-6): "))
    orden = input("¿Influye el orden? (s/n): ")
    todos = input("¿Entran todos los elementos? (s/n): ")
    repiten = input("¿Los elementos se repiten? (s/n): ")
    
    if tipo == 1:
        m = int(input("Ingrese m: "))
        n = int(input("Ingrese n: "))
        if orden == "s" and todos == "s":
            formula = "n!/(n-r)!"
            resultado = Formulas.variacion_ordinaria(m, n)
        elif orden == "s" and todos == "n":
            formula = "n!/(n-r)!"
            resultado = Formulas.variacion_ordinaria(m, n)
        elif orden == "n" and todos == "s":
            formula = "n^r"
            resultado = Formulas.variacion_repetida(m, n)
        else:
            formula = "n**r"
            resultado = Formulas.variacion_repetida(m, n)
    elif tipo == 2:
        if orden == "s" and todos == "s" and repiten == "s":
            formula = "n**r"
            resultado = Formulas.variacion_repetida(m, n)
        elif orden == "s" and todos == "s" and repiten == "n":
            formula = "n!/(n-r)!"
            resultado = Formulas.variacion_ordinaria(m, n)
        elif orden == "s" and todos == "n" and repiten == "s":
            formula = "n**r"
            resultado = Formulas.variacion_repetida(m, n)
        elif orden == "s" and todos == "n" and repiten == "n":
            formula = "n**r"
            resultado = Formulas.variacion_repetida(m, n)
        elif orden == "n" and todos == "s" and repiten == "s":
            formula = "n**r"
            resultado = Formulas.variacion_repetida(m, n)
        elif orden == "n" and todos == "s" and repiten == "n":
            formula = "n**r"
            resultado = Formulas.variacion_repetida(m, n)
        elif orden == "n" and todos == "n" and repiten == "s":
            formula = "(n+r-1)!/(r!(n-1)!) "
            resultado = Formulas.combinacion_repetida(m, n)
        else:
            formula = "n**r"
            resultado = Formulas.variacion_repetida(m, n)
    elif tipo == 3:
        if todos == "s":
            n = int(input("Ingresa n: "))
            formula = "n!"
            resultado = Formulas.permutacion_ordinaria(n)
        else:
            m = int(input("Ingrese m: "))
            n = int(input("Ingrese n: "))
            formula = "n!/(n-r)!"
            resultado = Formulas.variacion_ordinaria(m, n)
    elif tipo == 4:
        if repiten == "s":
            n = int(input("Ingrese el total de elementos: "))
            a = int(input("Cantidad de elemento 1: "))
            b = int(input("Cantidad de elemento 3: "))
            c = int(input("Cantidad de elemento 2: "))
            formula = "n!/a!*b!*c!"
            resultado = Formulas.permutacion_repetida(n, a, b, c)
        else:
            #Esta es la formula x
            formula = "n!/(n1!n2!...nk!)"
            resultado = Formulas.formula_x()
    elif tipo == 5:
        m = int(input("Ingrese m: "))
        n = int(input("Ingrese n: "))
        if todos == "s":
            formula = "n!/(r!(n-r)!) "
            resultado = Formulas.combinacion_ordinaria(m, n)
        else:
            formula = "n!/(r!(n-r)!)"
            resultado = Formulas.combinacion_ordinaria(m, n)
    else:
        if repiten == "s":
            formula = "(n+r-1)!/(r!(n-1)!) "
            resultado = Formulas.combinacion_repetida(m, n)
        else:
            formula = "n!/(r!(n-r)!) "
            resultado = Formulas.combinacion_ordinaria(m, n)

    return (formula, resultado)

# Ejemplo de uso
mostrar_menu()
formula, resultado = obtener_formula()
print("La fórmula a utilizar es:", formula)
print("El resultado es: ",resultado)

