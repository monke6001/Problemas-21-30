def suma_serie():
    n = int(input("Ingrese un número: "))
    suma = 0
    for i in range(1, n + 1):
        suma += i
    print("Suma de la serie:", suma)

suma_serie()
