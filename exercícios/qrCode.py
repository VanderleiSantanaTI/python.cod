import qrcode

imagem = qrcode.make("""
Nome: Rafaella Dantas
telefone : 2185125423
valor: R$365,23
estadia: 24H com pernoite
""")
imagem.save("Codigo_encomenda.png")
