import Formulas

def obtener_formula():
    orden = input("¿Influye el orden? (s/n): ").upper
    elementos = input("¿Entran todos los elementos? (s/n): ").upper
    repiten = input("¿Los elementos se repiten? (s/n): ").upper


    if orden == "s" and elementos == "n" and repiten =="n":
        m = int(input("Ingrese m: "))
        n = int(input("Ingrese n: "))
        formula = "m!/(m-n)!"
        resultado = Formulas.variacion_ordinaria(m, n)

        return (formula, resultado)

    elif orden == "s" and elementos == "n" and repiten =="s":
        m = int(input("Ingrese m: "))
        n = int(input("Ingrese n: "))
        formula = "m^n"
        resultado = Formulas.variacion_repetida(m, n)

        return (formula, resultado)

    elif orden == "s" and elementos == "s" and repiten =="n":
        m = int(input("Ingrese m: "))
        formula = "m!"
        resultado = Formulas.permutacion_ordinaria(m)

        return (formula, resultado)

    elif orden == "s" and elementos == "s" and repiten =="s":
        m = int(input("Ingrese m: "))
        a = int(input("Ingrese n: "))
        b = int(input("Ingrese n: "))
        c = int(input("Ingrese n: "))
        formula = "m!/a!*b!*c!"
        resultado = Formulas.permutacion_repetida(m, a, b, c)

        return (formula, resultado)
    
    elif orden == "n" and elementos == "n" and repiten =="n":
        m = int(input("Ingrese m: "))
        n = int(input("Ingrese n: "))
        formula = "m!/n!*(n-m)!"
        resultado = Formulas.combinacion_ordinaria(m, n)

        return (formula, resultado)

    elif orden == "n" and elementos == "n" and repiten =="s":
        m = int(input("Ingrese m: "))
        n = int(input("Ingrese n: "))
        formula = "(m+n-1)!/n!*(m-1)!"
        resultado = Formulas.combinacion_repetida(m, n)

        return (formula, resultado)
    
# Ejemplo de uso
formula, resultado = obtener_formula()
print("La fórmula a utilizar es:", formula)
print("El resultado es: ", resultado)
