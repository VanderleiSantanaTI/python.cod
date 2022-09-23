from time import sleep
import os
import pyautogui

# Configurações do experimento
# Substitua a linha abaixo pelo seu diretório de trabalho
caminho = r'C:\bomb\targets'
os.chdir(caminho)

# Substitua a linha abaixo pelo nome da imagem a ser localizada
arquivo = "x.png"


# Variáveis para controle da condição de parada
k = 0
n = 50

while True:
    # Procura a imagem
    local = pyautogui.locateCenterOnScreen(arquivo)

    # Se imagem for localizada
    if local is not None:
        pyautogui.moveTo(local, duration=0.2)
        pyautogui.click()
        print(f'Imagem localizada na posiçõa: {local}')
        break

    # Após n tentativas o programa encerra
    if k >= n:
        print('Imagem não localizada')
        break

    # Aguarda um pouco para tentar novamente
    sleep(0.25)
    k += 1
