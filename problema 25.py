import random

def generar_histograma():
    n = int(input("Ingrese la cantidad de datos a generar: "))
    datos = [random.randint(1, 10) for _ in range(n)]
    
    frecuencias = {}
    for num in datos:
        if num in frecuencias:
            frecuencias[num] += 1
        else:
            frecuencias[num] = 1
    
    print("\nHistograma:")
    for clave in sorted(frecuencias.keys()):
        print(f"{clave}: {'#' * frecuencias[clave]}")

generar_histograma()
