class Algoritmo:
    def __init__(self):
        pass

    @staticmethod
    def condicional(index):
        if index == True:
            valor = sim
            print(valor)
        else:
            valor = nao
            print(valor)

    @staticmethod
    def verdadeArgumento(verdadeiro):
        v = verdadeiro
        return v


    @staticmethod
    def falsoArgumento(falsos):
        f = falsos
        return f

    @staticmethod
    def escreva(index):
        print(f'{index}', end='')

    @staticmethod
    def escreval(index):
        print(f'{index}')

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
escreval = Algoritmo.escreval

leia = Algoritmo.leia
leia_inteiro = Algoritmo.leia_inteiro
leia_real = Algoritmo.leia_real

se = Algoritmo.condicional
verdade = Algoritmo.verdadeArgumento
falso = Algoritmo.falsoArgumento

sim = verdade(5)
nao = falso(56)

if __name__ == '__main__':


    escreva('digite um numero: ')
    numero1 = leia_inteiro()
    escreva('digite outro numero: ')
    numero2 = leia_real()
    res = numero1 * numero2
    escreval(res)
    se(5 > 2)






