import random

def lanzar():
    print("1. Lanzar un dado")
    print("2. Lanzar una moneda")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        print("Resultado del dado:", random.randint(1, 6))
    elif opcion == 2:
        print("Resultado de la moneda:", random.choice(["Cara", "Cruz"]))
    else:
        print("Opción no válida")

lanzar()
