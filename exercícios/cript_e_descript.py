import random

lista = ["#", "!", "$", "4", "6", "%", "~","F", "k", "J"]
v1 = random.choice(lista)
v2 = random.choice(lista)
print(v1, v2)


def crip(frase):
    valor0 = random.choice(lista)
    valor1 = random.choice(lista)
    valor2 = random.choice(lista)
    valor3 = random.choice(lista)
    mensagem = valor0 + valor1

    for i in frase:
        mensagem = mensagem + chr(ord(i) + 5) + valor1 + valor2 + valor3

    return mensagem


def descrip(mensagem):
    frase = ""

    for i in mensagem:
        frase = frase + chr(ord(i) - 5)

    return frase[2::4]  # Inicia do segundo digto e pula a cada 3 posições


palavra = crip("vanderler")
print(palavra)
print(descrip(palavra))

"""with open("C:/Users/Vanderlei/Desktop/newTest.txt", "w") as arquivo:
    texto = arquivo.write(palavra)
    print(texto)
sleep(3)"""

# with open("C:/Users/Vanderlei/Desktop/newTest.txt", "r") as arq:
#    texto2 = descrip(arq.read())
#   print(texto2)
