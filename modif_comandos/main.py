from typing import Any
import sys

class Escreva:
    def __init__(self, variavel: Any) -> None:
        self.variavel = variavel
        self.printar()

    def printar(self):
        sys.stdout.write(str(self.variavel))




class Leia:
    def __init__(self, mensagem: Any) -> None:
        self.mensagem = mensagem
        self.variavel = None
        self.obter_input()

    def obter_input(self):
        sys.stdout.write(self.mensagem)
        self.variavel = input()

    def __str__(self):
        return self.variavel
    


entrada = Leia("Digite algo: ")
Escreva(f"entrada: {entrada}")