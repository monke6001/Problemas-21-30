contactos = {}

def agregar_contacto():
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el teléfono: ")
    contactos[nombre] = telefono
    print("Contacto agregado.")

def mostrar_contactos():
    for nombre, telefono in contactos.items():
        print(f"{nombre}: {telefono}")

while True:
    print("\n1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Salir")

    opcion = int(input("Ingrese una opción: "))
    
    if opcion == 1:
        agregar_contacto()
    elif opcion == 2:
        mostrar_contactos()
    elif opcion == 3:
        break
    else:
        print("Opción no válida")
