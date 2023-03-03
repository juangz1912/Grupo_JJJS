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
        if orden == "s" and todos == "s":
            formula = "n!/(n-r)!"
        elif orden == "s" and todos == "n":
            formula = "n!/(n-r)!"
        elif orden == "n" and todos == "s":
            formula = "n^r"
        else:
            formula = "n**r"
    elif tipo == 2:
        if orden == "s" and todos == "s" and repiten == "s":
            formula = "n**r"
        elif orden == "s" and todos == "s" and repiten == "n":
            formula = "n!/(n-r)!"
        elif orden == "s" and todos == "n" and repiten == "s":
            formula = "n**r"
        elif orden == "s" and todos == "n" and repiten == "n":
            formula = "n**r"
        elif orden == "n" and todos == "s" and repiten == "s":
            formula = "n**r"
        elif orden == "n" and todos == "s" and repiten == "n":
            formula = "n**r"
        elif orden == "n" and todos == "n" and repiten == "s":
            formula = "(n+r-1)!/(r!(n-1)!) "
        else:
            formula = "n**r"
    elif tipo == 3:
        if todos == "s":
            formula = "n!"
        else:
            formula = "n!/(n-r)!"
    elif tipo == 4:
        if repiten == "s":
            formula = "n!/a!*b!*c!"
        else:
            formula = "n!/(n1!n2!...nk!)"
    elif tipo == 5:
        if todos == "s":
            formula = "n!/(r!(n-r)!) "
        else:
            formula = "n!/r!(n-r)!"
    else:
        if repiten == "s":
            formula = "(n+r-1)!/(r!(n-1)!) "
        else:
            formula = "n!/(r!(n-r)!) "

    return formula

# Ejemplo de uso
mostrar_menu()
formula = obtener_formula()
print("La fórmula a utilizar es:", formula)

