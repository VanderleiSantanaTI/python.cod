import pytesseract
import cv2
# explicação https://www.youtube.com/watch?v=Wx3SyNwZtsA
# passo 1: ler a imagem
imagem = cv2.imread("FotoVander.png")


# passo 2: mostrar o caminho onde foi instalado o tesseract pelo site
# https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
# pra instalar a linguagem-português do tesseract: https://github.com/tesseract-ocr/tessdata/blob/main/por.traineddata
caminho = r"C:\Program Files\Tesseract-OCR"

# passo 3: pedir pro tesseract extrair o texto da imagem
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
texto = pytesseract.image_to_string(imagem, lang="por")


print(texto)