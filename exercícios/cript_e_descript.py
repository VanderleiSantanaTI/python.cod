def crip(frase):
    mensagem = "oi"

    for i in frase:
        mensagem = mensagem + chr(ord(i) + 5)

    return mensagem


def descrip(mensagem):
    frase = "oioi"
    for i in mensagem:
        frase = frase + chr(ord(i) - 5)

    return frase


palavra = (crip("zé santana"))
print(palavra)
print(descrip(palavra))

"""with open("C:/Users/Vanderlei/Desktop/newTest.txt", "w") as arquivo:
    texto = arquivo.write(palavra)
    print(texto)
sleep(3)"""

# with open("C:/Users/Vanderlei/Desktop/newTest.txt", "r") as arq:
#    texto2 = descrip(arq.read())
#   print(texto2)
