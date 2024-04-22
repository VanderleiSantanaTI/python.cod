from operacoes import Operacoes
class Acao(Operacoes):
    def __init__(self, nome, valor):
        super().__init__(nome)
        self.valor = valor

