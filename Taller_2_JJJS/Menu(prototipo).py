import Formulas

def obtener_formula():
    resultados = []
    for i in range(2):
        multi = input("¿entra el principio multiplicativo? (s/n): ").lower()
        adi = input("¿entra el principio aditivo? (s/n): ").lower()
        orden = input("¿Influye el orden? (s/n): ").lower()
        elementos = input("¿Entran todos los elementos? (s/n): ").lower()
        repiten = input("¿Los elementos se repiten? (s/n): ").lower()


        if orden == "s" and elementos == "n" and repiten =="n":
            formula = "m!/(m-n)!"
            print(formula)
            m = int(input("Ingrese la población total: "))
            n = int(input("Ingrese la muestra(cantidad tomada): "))
            resultado = Formulas.variacion_ordinaria(m, n)
            if adi == "s" or multi == "s":
                resultados.append(resultado)
            continuar = input("¿deseas hacer una nueva iteración?(s/n): ").lower()
            if continuar == "s":
                continue
            else:
                break
        

        elif orden == "s" and elementos == "n" and repiten =="s":
            formula = "m^n"
            print(formula)
            m = int(input("Ingrese la población total: "))
            n = int(input("Ingrese la muestra(cantidad tomada): "))
            resultado = Formulas.variacion_repetida(m, n)
            if adi == "s" or multi == "s":
                resultados.append(resultado)
            continuar = input("¿deseas hacer una nueva iteración?(s/n): ").lower()
            if continuar == "s":
                continue
            else:
                break


        elif orden == "s" and elementos == "s" and repiten =="n":
            formula = "m!"
            print(formula)
            m = int(input("Ingrese la población total: "))
            resultado = Formulas.permutacion_ordinaria(m)
            if adi == "s" or multi == "s":
                resultados.append(resultado)
            continuar = input("¿deseas hacer una nueva iteración?(s/n): ").lower()
            if continuar == "s":
                continue
            else:
                break


        elif orden == "s" and elementos == "s" and repiten =="s":
            formula = "m!/a!*b!*c!"
            print(formula)
            m = int(input("Ingrese la población total: "))
            a = int(input("Ingrese la muestra(cantidad 1): "))
            b = int(input("Ingrese la muestra(cantidad 2): "))
            c = int(input("Ingrese la muestra(cantidad 3): "))
            resultado = Formulas.permutacion_repetida(m, a, b, c)
            if adi == "s" or multi == "s":
                resultados.append(resultado)
            continuar = input("¿deseas hacer una nueva iteración?(s/n): ").lower()
            if continuar == "s":
                continue
            else:
                break

    
        elif orden == "n" and elementos == "n" and repiten =="n":
            formula = "m!/n!*(n-m)!"
            print(formula)
            m = int(input("Ingrese la población total: "))
            n = int(input("Ingrese la muestra(cantidad tomada): "))
            resultado = Formulas.combinacion_ordinaria(m, n)
            if adi == "s" or multi == "s":
                resultados.append(resultado)
            continuar = input("¿deseas hacer una nueva iteración?(s/n): ").lower()
            if continuar == "s":
                continue
            else:
                break

        elif orden == "n" and elementos == "n" and repiten =="s":
            formula = "(m+n-1)!/n!*(m-1)!"
            print(formula)
            m = int(input("Ingrese la población total: "))
            n = int(input("Ingrese la muestra(cantidad tomada): "))
            resultado = Formulas.combinacion_repetida(m, n)
            if adi == "s" or multi == "s":
                resultados.append(resultado)
            continuar = input("¿deseas hacer una nueva iteración?(s/n): ").lower()
            if continuar == "s":
                continue
            else:
                break
    if len(resultados) > 1 and multi == "s":
        resultado = resultados[0] * resultados[1]
    elif len(resultados) > 1 and adi == "s":
        resultado = resultados[0] + resultados[1]
    return resultado
    
    
# Ejemplo de uso
resultado = obtener_formula()
print("El resultado es: ", resultado)