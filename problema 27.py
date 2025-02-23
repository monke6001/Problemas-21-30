def conversor():
    print("Seleccione la conversión:")
    print("1. Kilómetros a millas")
    print("2. Celsius a Fahrenheit")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        km = float(input("Ingrese kilómetros: "))
        print(f"{km} km son {km * 0.621371} millas")
    elif opcion == 2:
        celsius = float(input("Ingrese grados Celsius: "))
        print(f"{celsius}°C son {(celsius * 9/5) + 32}°F")
    else:
        print("Opción no válida")

conversor()
