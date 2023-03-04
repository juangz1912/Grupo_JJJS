def factorial(numero): #Función recursiva del factorial que utilizaré para las demás fórmulas
  if numero==0 :
    return 1
  else:
      times = numero*(factorial(numero-1))
      return times

def formula_x():
   numerador = input("Ingrese el 'n' del numerador: ")
   numerador = factorial(numerador)
   numero_n = int(input("Cuantos n en el denominador? "))
   denominador = 1
   for i in range(1, numero_n + 1):
      print("Ingrese n",i)
      n = input()
      denominador = denominador*factorial(n)
   formula = numerador // denominador
   return formula

def variacion_ordinaria(m,n): #siendo m = el total de elementos y n = elementos tomados
   formula = factorial(m)//factorial(m-n)
   return formula

def variacion_repetida(base,exponente): # siendo la base = el total de elementos dados y el exponente = cantidad de elementos pedidos
   formula = base**exponente
   return formula

def permutacion_ordinaria(numero): # el número seria el total de elementos dados
   formula = factorial(numero)
   return formula

def permutacion_repetida(n,a,b,c): # siendo n = el total de elementos, a = cantidad de elemento 1, b = cantidad de elemento 2 y c = cantidad de elemento 3 
   formula = factorial(n)//((factorial(a))*(factorial(b))*(factorial(c)))
   return formula

def combinacion_ordinaria(n,m): #siendo m = el total de elementos y n = elementos tomados
   formula = factorial(n)//((factorial(m))*(factorial(n-m)))
   return formula

def combinacion_repetida(m,n): #siendo m = el total de elementos y n = elementos tomados
   formula = factorial(m+n-1)//((factorial(n))*(factorial(m-1)))
   return formula
