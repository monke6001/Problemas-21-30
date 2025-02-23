import random

def calcular_estadisticas():
    n = int(input("Ingrese la cantidad de datos a generar: "))
    datos = [random.randint(1, 100) for _ in range(n)]
    
    media = sum(datos) / n
    datos_ordenados = sorted(datos)
    mediana = datos_ordenados[n//2] if n % 2 != 0 else (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2

    print("Datos generados:", datos)
    print("Media:", media)
    print("Mediana:", mediana)

calcular_estadisticas()
