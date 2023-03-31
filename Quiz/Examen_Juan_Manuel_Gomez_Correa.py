def menuInicial():
    numeroInt = int(input("Digite el número: "))
    print(cantidadDigitos(numeroInt))
    print("NO RECURSIVO: ", cantidadDigitosNoR(numeroInt))

def cantidadDigitos(numeroInt):
    if numeroInt == 0:
        return 0
    numeroInt = numeroInt//10
    return cantidadDigitos(numeroInt) + 1

def cantidadDigitosNoR(numeroInt):          #O(n)
    contador = 0                        #O(1)
    while numeroInt != 0:               #O(n)
        numeroInt = numeroInt//10       #O(n)
        contador += 1                   #O(n)

    # O(1) + O(n) + O(n) + O(n)
    # = 3n+1 = O(n)
    
    return contador                     #O(n)

menuInicial()
print("Respuesta No Recuersiva: ", cantidadDigitosNoR(123456789)) #O(n)
