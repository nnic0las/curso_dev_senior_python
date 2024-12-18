class CuentaBancaria:

    def __init__(self, titular, saldo, clave):
        self.titular = titular
        self._saldo = saldo
        self.__clave = clave
        

    def depositar(self, cantidadDeposito):
        self._saldo += cantidadDeposito
        return f'Deposito exitoso. Saldo actual{self._saldo}'

    def retirar(self, cantidadRetiro):
        if cantidadRetiro > self._saldo:
            return 'Fondos insuficiente'
        self._saldo -= cantidadRetiro
        return f'Retiro exitoso. El saldo actual es {self._saldo}'
    
    def modificarClave(self, nuevaClave):
        self.__clave = nuevaClave
        return f'Clave modificada de forma exitosa. La  nueva clave es: {self.__clave}'
    
CuentaBancaria1 =CuentaBancaria("nicolas mendoza", 10000000, 1234)

print(CuentaBancaria1.titular)
print(CuentaBancaria1._saldo)

print(CuentaBancaria1.depositar(500000))
print(CuentaBancaria1.depositar(500000))
print(CuentaBancaria1.retirar(100000))
print(CuentaBancaria1.retirar(100000))
print(CuentaBancaria1.retirar(100000))

print(CuentaBancaria1.modificarClave(2121))



