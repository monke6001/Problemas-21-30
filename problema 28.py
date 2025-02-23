class CuentaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se depositaron {cantidad}. Saldo actual: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se retiraron {cantidad}. Saldo actual: {self.saldo}")
        else:
            print("Fondos insuficientes")

cuenta = CuentaBancaria()

while True:
    print("\n1. Depositar")
    print("2. Retirar")
    print("3. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        cuenta.depositar(cantidad)
    elif opcion == 2:
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        cuenta.retirar(cantidad)
    elif opcion == 3:
        break
    else:
        print("Opción no válida")
