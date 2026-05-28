"""
Taller: Encapsulacion.
Se protegen atributos sensibles y se exponen por metodos y propiedades.
"""


class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = float(saldo_inicial)

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto <= 0:
            return False, "El monto debe ser mayor a 0."
        self.__saldo += monto
        return True, f"Deposito exitoso. Saldo actual: ${self.__saldo:,.2f}"

    def retirar(self, monto):
        if monto <= 0:
            return False, "El monto debe ser mayor a 0."
        if monto > self.__saldo:
            return False, "Fondos insuficientes."
        self.__saldo -= monto
        return True, f"Retiro exitoso. Saldo actual: ${self.__saldo:,.2f}"


def main():
    cuenta = CuentaBancaria("Luisa", 120000)
    print("=== TALLER: ENCAPSULACION ===")
    print(f"Titular: {cuenta.titular}")
    print(f"Saldo inicial: ${cuenta.saldo:,.2f}")

    print(cuenta.depositar(30000)[1])
    print(cuenta.retirar(50000)[1])
    print(cuenta.retirar(500000)[1])

    print("\nIntento de acceso directo a atributo privado:")
    print("cuenta.__saldo -> AttributeError esperado")


if __name__ == "__main__":
    main()