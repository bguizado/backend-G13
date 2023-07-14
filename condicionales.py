a = 10
b = 5

if a < b:
    print("Se cumple la condicion")
elif a == b:
    print("Se cumple la condicion 2")
else:
    print("No se cumple la condicion")

if a > b and a == 10:
    print("Se cumple la condicion 3")

if a > b or a == 10:
    print("Se cumple la condicion 4")

user = None

if not user:
    print("No hay usuario")
