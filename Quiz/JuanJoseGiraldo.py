#Punto 2
def potencia(f, n):
    F = 1 #O(1)
    for i in range(n):#O(n)
        F = F * f #O(n)
    return F #O(n)

#Big O =1(1) + 3(n)

print(potencia(5,5))

def potencia_recursivo(f,n,R=1):
    if n == 0:
        return R
    else:
        R = R*f
        N = n-1
        return potencia_recursivo(f, N, R)

print(potencia_recursivo(5,5))

#Punto 3
def factorial(numero):
  if numero==0 :
    return 1
  else:
      times = numero*(factorial(numero-1))
      return times

def permutacion_ordinaria(numero):
    formula = factorial(numero)
    return formula

print(permutacion_ordinaria(5))
