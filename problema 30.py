def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

num = int(input("Ingrese un número para calcular su factorial: "))
print(f"Factorial de {num}: {factorial(num)}")
