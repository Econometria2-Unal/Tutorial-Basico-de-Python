class CuentaBancaria:
    # Variable de clase: compartida por todas las cuentas
    nombre_banco = "Banco Nacional"
    total_cuentas = 0

    def __init__(self, titular, saldo=0):
        self.titular = titular      # nombre del titular
        self.saldo = saldo          # saldo inicial
        CuentaBancaria.total_cuentas += 1  # cada cuenta nueva incrementa el contador

    def depositar(self, monto):
        if monto <= 0:
            return "El depósito debe ser positivo."
        self.saldo += monto
        return f"Depositado {monto}. Nuevo saldo: {self.saldo}"

    def retirar(self, monto):
        if monto <= 0:
            return "El retiro debe ser positivo."
        if monto > self.saldo:
            return "Fondos insuficientes."
        self.saldo -= monto
        return f"Retirado {monto}. Nuevo saldo: {self.saldo}"

    @classmethod
    def info_banco(cls):
        # cls se refiere a la clase misma, no a una instancia
        return f"{cls.nombre_banco} | total_cuentas={cls.total_cuentas}"

    def __str__(self):
        return f"{self.__class__.__name__}(titular={self.titular}, saldo={self.saldo})"


# CuentaAhorros hereda de CuentaBancaria (es un tipo especial de cuenta)
class CuentaAhorros(CuentaBancaria):
    def __init__(self, titular, saldo=0, tasa_interes=0.02):
        super().__init__(titular, saldo)     # reutiliza el __init__ del padre
        self.tasa_interes = tasa_interes     # atributo exclusivo de esta subclase

    def aplicar_interes(self):
        interes = self.saldo * self.tasa_interes
        self.saldo += interes
        return f"Interés aplicado: {interes:.2f}. Nuevo saldo: {self.saldo:.2f}"


# Otra subclase que modifica el comportamiento de retirar
class CuentaEstudiante(CuentaBancaria):
    limite_retiro = 50  # límite de retiro por transacción para estudiantes

    def retirar(self, monto):
        # los estudiantes no pueden retirar más del límite por transacción
        if monto > CuentaEstudiante.limite_retiro:
            return f"Límite excedido. Máximo por retiro: {CuentaEstudiante.limite_retiro}."
        return super().retirar(monto)  # si pasa el filtro, usa el retirar del padre



