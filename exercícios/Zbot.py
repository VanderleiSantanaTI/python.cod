from datetime import date
from time import sleep
import os
import pyautogui

pyautogui.alert("***Projeto cod: Vanderlei S Andrade****"
                "Versao 3.1 ***Abra Antes o BombCrypto :-)")


# Substitua a linha abaixo pelo seu diretório de trabalho
caminho = r'C:\BombCrypto\target'
os.chdir(caminho)
# Substitua a linha abaixo pelo nome da imagem a ser localizada
ConnectWallet = "connect-wallet-ze.png"
Assinar = "select-wallet-2-ze.png"
fotobomb = "fotobomb.png"
ok = "ok-ze.png"
SetaBack = "go-back-arrow.png"
HeroIcon = "hero-icon.png"
WorkAll = "all-gree.png"
Xsair = "x.png"
barra = "barra.png"
OneWork = "go-work.png"
Scroll = "scroll.png"
Upgrade = "upgrade.png"
# Variáveis para controle da condição de parada
k = 0
n = 2


# Procura a imagem
def ConnectWallet_local_img():
    sleep(3)
    print("Projeto : Vanderlei S Andrade *** cel :+55(11)98414-2128")
    local = pyautogui.locateCenterOnScreen(ConnectWallet)
    sleep(1)
    # Se imagem for localizada
    if local is not None:
        pyautogui.moveTo(local, duration=2)
        pyautogui.click(local)
        print(f'Imagem localizada na posicao: {local}')
        sleep(15)
    else:
        print("imagem 'connect-wallet' nao localizada")


def Assinar_local_img():
    sleep(2)
    local1 = pyautogui.locateCenterOnScreen(Assinar)
    sleep(1)
    if local1 is not None:
        pyautogui.moveTo(local1, duration=2)
        pyautogui.click(local1)
        print(f'Imagem localizada na posicao: {local1}')
        sleep(10)
    else:
        print("imagem 'assinar' nao localizada")


def fotobomb_local_img():
    sleep(1)
    local2 = pyautogui.locateCenterOnScreen(fotobomb)
    sleep(1)
    if local2 is not None:
        pyautogui.moveTo(local2, duration=2)
        pyautogui.click()
        print(f'Imagem localizada na posicao: {local2}')
        sleep(2)
    else:
        print("imagem 'bombCrypto-central' nao localizada")


def ok_local_img():
    sleep(2)
    local3 = pyautogui.locateCenterOnScreen(ok)
    if local3 is not None:

        pyautogui.moveTo(local3, duration=2)
        pyautogui.click()
        print(f'Imagem localizada na posicao: {local3}')
    else:
        print("imagem 'OK' nao localizada")


def SetaBack_local_img():
    sleep(10)
    local4 = pyautogui.locateCenterOnScreen(SetaBack)
    sleep(1)
    # Se imagem for localizada
    if local4 is not None:

        pyautogui.moveTo(local4, duration=2)
        pyautogui.click(local4)
        print(f'Imagem localizada na posicao: {local4}')
    else:
        print("tentativa na imagem go-back-arrow frustada ")


def HeroIcon_local_img():
    sleep(2)
    local5 = pyautogui.locateCenterOnScreen(HeroIcon)
    sleep(1)
    if local5 is not None:
        pyautogui.moveTo(local5, duration=2)
        pyautogui.click(local5)
        print(f'Imagem hero-icon na posicao:', {local5})
    else:
        print("imagem 'hero-icon' nao localizada")


def WorkAll_local_img():
    sleep(3)
    local6 = pyautogui.locateCenterOnScreen(WorkAll)
    sleep(1)
    if local6 is not None:
        pyautogui.moveTo(local6, duration=2)
        pyautogui.click(local6)
        print(f'Imagem all-gree na posicao: {local6}')
    else:
        print("imagem 'all-gree' nao localizada")


def Xsair_local_img():
    sleep(1)
    local7 = pyautogui.locateCenterOnScreen(Xsair)
    if local7 is not None:
        pyautogui.moveTo(local7, duration=2)
        pyautogui.click(local7)
        print(f'Imagem (X) na posicao: {local7}')
        sleep(2)
    else:
        print("imagem 'X' nao localizada")


def Click_one_work():
    try:
        pyautogui.PAUSE = 0.5

        for i in range(4):
            a = 0
            while a <= 3:
                l1 = pyautogui.locateCenterOnScreen(barra)

                if l1 is not None:
                    b = 0
                    while b <= 5:
                        local9 = pyautogui.locateCenterOnScreen(OneWork)

                        if local9 is not None:

                            try:

                                x, y, w, h = pyautogui.locateOnScreen(OneWork)
                                ponto = pyautogui.locateCenterOnScreen("barra.png", region=(x - w * 3, y, w * 6, h * 2))

                                if ponto is not None:

                                    pyautogui.moveTo((x + w / 2, y + h / 2), duration=2)
                                    print(ponto)
                                    pyautogui.click()
                                else:
                                    pass
                            except:

                                pass

                        else:
                            pass
                        b += 1
                else:
                    pass

                a += 1
            x, y, w, h = pyautogui.locateOnScreen(Scroll)
            pyautogui.moveTo((x - x / 4, y * 2.5, w, h), duration=2)
            pyautogui.mouseDown()
            pyautogui.moveTo((x - x / 4, y * 1.5, w, h), duration=2)
            pyautogui.mouseUp()
    except:
        pass


def Click_Central():
    seta = pyautogui.locateCenterOnScreen(SetaBack)
    if seta is not None:
        x, y = pyautogui.size()
        print(f'Resolução da tela ({x} x {y})')
        print(f'cliclk central=>({x - x / 2:,.0f} x {y - y / 2:,.0f})')
        pyautogui.moveTo(x - x / 2, y - y / 2, duration=2)
        pyautogui.click()
    else:
        print("Imagem **seta-back** nao localizada")


def _go_work_12345():
    for i in range(4):
        go_work1()
        go_work1()
        go_work2()
        go_work3()
        go_work4()
        go_work5()
        go_work1()
        go_work2()
        go_work3()
        go_work4()
        go_work5()
        go_work1()
        go_work2()
        go_work3()
        go_work4()
        go_work5()
        go_work1()
        go_work2()
        go_work3()
        go_work4()
        go_work5()
        go_work1()
        go_work2()
        go_work3()
        go_work5()
        scroll()
    go_work1()
    go_work1()
    go_work1()
    go_work1()
    go_work1()
    go_work2()
    go_work2()
    go_work2()
    go_work2()
    go_work2()
    go_work3()
    go_work3()
    go_work3()
    go_work3()
    go_work3()
    go_work4()
    go_work4()
    go_work4()
    go_work4()
    go_work4()
    go_work5()
    go_work5()
    go_work5()
    go_work5()
    go_work5()


def go_work1():
    try:

        pyautogui.PAUSE = 0.7
        barra1 = pyautogui.locateOnScreen("barra.png")
        locall = pyautogui.locateOnScreen("go-work.png")
        arg0 = int(locall[0])
        arg1 = int(locall[1])
        arg2 = int(locall[2])
        arg3 = int(locall[3])

        if barra1 is not None:
            try:
                x, y, w, h = pyautogui.locateOnScreen("go-work.png", region=(arg0 - arg2, arg1, arg2 * 5, arg3 * 5))
                ponto = pyautogui.locateCenterOnScreen("barra.png", region=(x - w * 3, y, w * 6, h * 2))
                print(ponto)

                if ponto is not None:
                    pyautogui.moveTo((x + w / 2, y + h / 2), duration=1)
                    print(ponto)
                    pyautogui.click()

            except:

                pass



    except:
        pass


def go_work2():
    try:

        pyautogui.PAUSE = 0.7
        barra1 = pyautogui.locateOnScreen("barra.png")
        locall = pyautogui.locateOnScreen("go-work.png")
        arg0 = int(locall[0])
        arg1 = int(locall[1])
        arg2 = int(locall[2])
        arg3 = int(locall[3])

        if barra1 is not None:
            try:
                x, y, w, h = pyautogui.locateOnScreen("go-work.png",
                                                      region=(arg0 - arg2, arg1 + arg3, arg2 * 5, arg3 * 5))
                ponto = pyautogui.locateCenterOnScreen("barra.png", region=(x - w * 3, y, w * 6, h * 2))
                print(ponto)

                if ponto is not None:
                    pyautogui.moveTo((x + w / 2, y + h / 2), duration=1)
                    print(ponto)
                    pyautogui.click()

            except:

                pass



    except:
        pass


def go_work3():
    try:

        pyautogui.PAUSE = 0.7
        barra1 = pyautogui.locateOnScreen("barra.png")
        locall = pyautogui.locateOnScreen("go-work.png")
        arg0 = (locall[0])
        arg1 = (locall[1])
        arg2 = (locall[2])
        arg3 = (locall[3])

        if barra1 is not None:
            try:
                x, y, w, h = pyautogui.locateOnScreen("go-work.png",
                                                      region=(arg0 - arg2, arg1 + arg3 * 2, arg2 * 5, arg3 * 5))
                sleep(1)
                ponto = pyautogui.locateCenterOnScreen("barra.png", region=(x - w * 3, y, w * 6, h * 2))
                print(ponto)

                if ponto is not None:
                    pyautogui.moveTo((x + w / 2, y + h / 2), duration=1)
                    print(ponto)
                    pyautogui.click()


            except:

                pass



    except:
        pass


def go_work4():
    try:

        pyautogui.PAUSE = 0.7
        barra1 = pyautogui.locateOnScreen("barra.png")
        locall = pyautogui.locateOnScreen("go-work.png")
        arg0 = (locall[0])
        arg1 = (locall[1])
        arg2 = (locall[2])
        arg3 = (locall[3])

        if barra1 is not None:
            try:
                x, y, w, h = pyautogui.locateOnScreen("go-work.png",
                                                      region=(arg0 - arg2, arg1 + arg3 * 4, arg2 * 5, arg3 * 5))
                ponto = pyautogui.locateCenterOnScreen("barra.png", region=(x - w * 3, y, w * 6, h * 2))
                print(ponto)

                if ponto is not None:
                    pyautogui.moveTo((x + w / 2, y + h / 2), duration=1)
                    print(ponto)
                    pyautogui.click()


            except:

                pass



    except:
        pass


def go_work5():
    try:

        pyautogui.PAUSE = 0.7
        barra1 = pyautogui.locateOnScreen("barra.png")
        locall = pyautogui.locateOnScreen("go-work.png")
        arg0 = (locall[0])
        arg1 = (locall[1])
        arg2 = (locall[2])
        arg3 = (locall[3])

        if barra1 is not None:
            try:
                x, y, w, h = pyautogui.locateOnScreen("go-work.png",
                                                      region=(arg0 - arg2, arg1 + arg3 * 6, arg2 * 5, arg3 * 5))
                ponto = pyautogui.locateCenterOnScreen("barra.png", region=(x - w * 3, y, w * 6, h * 2))
                print(ponto)

                if ponto is not None:
                    pyautogui.moveTo((x + w / 2, y + h / 2), duration=1)
                    print(ponto)
                    pyautogui.click()


            except:

                pass



    except:
        pass


def scroll():
    scr = pyautogui.locateCenterOnScreen(Upgrade)
    if scr is not None:
        x, y, w, h = pyautogui.locateOnScreen(Upgrade)
        pyautogui.moveTo((x - x*0.75, y, w, h), duration=1.5)
        pyautogui.mouseDown()
        pyautogui.moveTo((x - x*0.75, y/1.8, w, h), duration=1.5)
        sleep(0.5)
        pyautogui.mouseUp()
    else:
        pass




while True:

    data_atual = date.today()
    licence_time = date(2022, 3, 17)
    if data_atual <= licence_time:
        print('Expirará na data {}'.format(licence_time))
        while k < n:
            ConnectWallet_local_img()
            Assinar_local_img()
            fotobomb_local_img()
            sleep(9)
            ok_local_img()
            sleep(10)
            print("-*-*_" * 10)
            # Aguarda um pouco para tentar novamente
            sleep(0.25)
            k += 1
        # Proxima etapa do processo
        _go_work_12345()
        Xsair_local_img()
        fotobomb_local_img()
        Click_Central()

        for i in range(5):
            print(" 3 min p/ retomada")
            sleep(60)
            print(" 2 min p/ retomada")
            sleep(60)
            print(" 1 min p/ retomada")
            sleep(60)
            print("Retomamos a operação ")
            ConnectWallet_local_img()
            Assinar_local_img()
            sleep(10)
            ok_local_img()
            SetaBack_local_img()
            fotobomb_local_img()
            sleep(2)
            Click_Central()
    else:
        print('Expirou')
        print('Entre em contato com o *** cel :+55(11)98414-2128\npara prolongar sua licenca' )
        sleep(10)
        break