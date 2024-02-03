import qrcode

imagem = qrcode.make("RafaellaDantas")
imagem.save("Codigo_encomenda.png")
