class Algoritmo:
    def __init__(self):
        pass

    @staticmethod
    def escreva(nome):
        print(f'{nome}')

    @staticmethod
    def leia() -> str:
        entrada = (input())
        return entrada

    @staticmethod
    def leia_inteiro() -> int:
        entrada = int(input())
        return entrada

    @staticmethod
    def leia_real() -> float:
        entrada = float(input())
        return entrada

# Definindo funções globais
escreva = Algoritmo.escreva
leia = Algoritmo.leia
leia_inteiro = Algoritmo.leia_inteiro
leia_real = Algoritmo.leia_real

if __name__ == '__main__':

    escreva('digite um numero: ')
    numero1 = leia_inteiro()
    escreva('digite outro numero: ')
    numero2 = leia_real()
    res = numero1*numero2
    escreva(res)

