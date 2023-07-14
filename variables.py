numero = 5
print(numero)

if numero == 5:
    print("El numero es igual a 5")


numero = 10

if numero == 5:
    print("El numero es igual a 5")


numero1, numero2, numero3 = 5, 10, 15

a = "Fácil"

def miFuncion():
    a = "Hermoso"
    print("Python es " + a)

miFuncion()
print("Python es " + a)

def miFuncion2():
    global a
    a = "Hermosoooo"

miFuncion2()
print("Python es " + a)
