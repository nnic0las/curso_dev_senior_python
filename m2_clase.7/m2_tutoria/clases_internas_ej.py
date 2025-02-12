class CuentaBanco:
    def __init__(self,titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    class Transaccion:
        def __init__(self, cuenta, monto, tipo):
            self.cuenta = cuenta
            self.monto = monto
            self.tipo = tipo

        def ejecutar(self):
            if self.tipo == "deposito":
                self.cuenta.saldo += self.monto
            elif self.tipo =="retiro" and self.cuenta.saldo >= self.monto:
                self.cuenta.saldo -= self.monto

            else:
                print(f"saldo actual: {self.cuenta.saldo}")
cuenta = CuentaBanco("nicolas", 1000)
deposito = cuenta.Transaccion(cuenta, 500, "deposito")
deposito.ejecutar()

retiro = cuenta.Transaccion(cuenta, 400, "retiro")
retiro.ejecutar()

