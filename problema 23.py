def crear_matriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            valor = int(input(f"Ingrese el valor para [{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def suma_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

def multiplicacion_matrices(A, B):
    n = len(A)
    resultado = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                resultado[i][j] += A[i][k] * B[k][j]
    return resultado

n = int(input("Ingrese el tamaño de la matriz (n x n): "))

print("Ingrese la primera matriz:")
A = crear_matriz(n)

print("Ingrese la segunda matriz:")
B = crear_matriz(n)

print("\nSuma de matrices:")
imprimir_matriz(suma_matrices(A, B))

print("\nProducto de matrices:")
imprimir_matriz(multiplicacion_matrices(A, B))
