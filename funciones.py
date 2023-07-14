def suma(a,b):
    return a+b

print(suma(2,3))

def resta(a,b):
    return a-b

print(resta(2,10))

def multiplicacion(a,b):
    return a*b

print(multiplicacion(2,4))

def division(a,b):
    return a/b

print(division(2,4))

def division(a,b):
    if b == 0:
        print("No se puede dividir por 0")
        return
    return a/b

#recursividad en funciones
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

print(factorial(5))