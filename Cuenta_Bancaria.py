class CuentaBancaria:
    def __init__(self, Titular, Saldo_inicial):
        self.Titular = Titular 
        self._Historial = []
        self.__Saldo_inicial = Saldo_inicial
        self.__Saldo = 0
        self.Depositar(Saldo_inicial)

    def get_Saldo(self):
        return self.__Saldo
        
    def set_Saldo(self, monto):
        if monto < 0:
            print("No se puede establecer un  saldo negativo")
            return
        self.__Saldo = monto

    def Depositar(self, monto):
        if monto <= 0:
            print("El monto a depositar debe ser positivo")
            return 
        self.__Saldo += monto
        self._Historial.append(f"Despositar + {monto}")
    def retirar(self, monto):
        if monto <= 0:
            print( " El monto a retirar debe ser positivo")
            return 
        if monto > self.__Saldo:
            print(" No se puede retirar màs de los tienes en la cuenta")
            return 
        self.__Saldo -= monto 
        self._Historial.append(f"retiro: -{monto}")
        
    def Ver_Saldo(self):
        print(f"saldo actual: {self.get_Saldo()}")

    def Ver_Historial(self):
        print("Historial de transacciones:")
        for Transaccion in self._Historial:
            print(Transaccion)
def main ():
    Cuenta1 = CuentaBancaria("Nicole Ramirez Betancur", 50000)
    Cuenta1.Depositar(20000)
    Cuenta1.retirar(10000)
    print("Esta es la cuenta de:",Cuenta1.Titular)
    
    Cuenta1.Ver_Saldo()

    Cuenta1.Ver_Historial()
main()