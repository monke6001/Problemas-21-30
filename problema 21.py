import math

def calcular_figuras():
    print("Seleccione la figura:")
    print("1. Círculo (Área)")
    print("2. Esfera (Volumen)")
    print("3. Cuadrado (Área)")
    print("4. Cubo (Volumen)")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        radio = float(input("Ingrese el radio: "))
        print("Área del círculo:", math.pi * radio**2)
    elif opcion == 2:
        radio = float(input("Ingrese el radio: "))
        print("Volumen de la esfera:", (4/3) * math.pi * radio**3)
    elif opcion == 3:
        lado = float(input("Ingrese el lado: "))
        print("Área del cuadrado:", lado**2)
    elif opcion == 4:
        lado = float(input("Ingrese el lado: "))
        print("Volumen del cubo:", lado**3)
    else:
        print("Opción no válida")

calcular_figuras()
