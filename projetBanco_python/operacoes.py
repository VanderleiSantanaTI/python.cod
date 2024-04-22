from clientes import Clientes

class Operacoes(Clientes):
    def __init__(self, nome):
        super().__init__(nome)
        self.saldo = 0
         
    def depositarDinheiro(self, valor):
        self.saldo += valor
        

    def sacarDinheiro(self, valor):
        self.saldo -= valor 
        if self.saldo < 0:
            self.saldo = 0
            print("Saldo insuficiente" + str(self.saldo))
            

    def saldoDinheiro(self):
        return print(f"Cliente: {self.name} esta com R${self.saldo} de saldo")        
