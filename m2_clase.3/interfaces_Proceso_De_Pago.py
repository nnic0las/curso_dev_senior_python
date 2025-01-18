##interfaces python
from abc import ABC, abstractmethod

class ProcesoPago(ABC):

    @abstractmethod
    def procesoPago(self, cantidad: float) -> None:
        pass

    @abstractmethod
    def reembolsoPago(self, transaccionId: str) -> None:
        pass

class Paypal(ProcesoPago):

    def procesoPago(self, cantidad: float) -> None:
        print(f"procesando pago de ${cantidad} por paypal")

    def reembolsoPago(self, transaccionId: str) -> None:
        print (f"reembolsando id transaccion numero {transaccionId} ")

class Stripe(ProcesoPago):

    def procesoPago(self, cantidad: float) -> None:
        print(f"Procesando pago de ${cantidad} por stripe")

    def reembolsoPago(self, transaccionId: float) -> None:
        print(f"reembolsando id transaccion numero {transaccionId} por Stripe")


if __name__ == "__main__":
    procesoPaypal = Paypal()
    procesoStripe = Stripe()

    procesoPaypal.procesoPago(500.0)
    procesoPaypal.reembolsoPago("fds")

    procesoStripe.procesoPago(1000.0)
    procesoStripe.reembolsoPago("fds")


