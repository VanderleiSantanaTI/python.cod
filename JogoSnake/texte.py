import keyboard
from pynput import keyboard as pynput_keyboard

# Variável para rastrear se a tecla Alt está sendo pressionada
alt_pressed = False

def on_press(key):
    global alt_pressed

    try:
        if key.char == 'a' and alt_pressed:
            print("Combinação de teclas Alt + A pressionada.")
            # Adicione a ação desejada ao detectar Alt + A

    except AttributeError:
        # Se não for uma tecla de caractere, verifica se é uma tecla especial
        if key == pynput_keyboard.Key.alt:
            alt_pressed = True

def on_release(key):
    global alt_pressed

    try:
        if key.char == 'a':
            # Adicione ação desejada ao liberar a tecla 'a'
            pass

    except AttributeError:
        # Se não for uma tecla de caractere, verifica se é uma tecla especial
        if key == pynput_keyboard.Key.alt:
            alt_pressed = False

# Adiciona um ouvinte global para eventos de teclado usando a biblioteca keyboard
keyboard.hook(on_press)
keyboard.hook(on_release)

# Mantém o programa em execução
keyboard.wait()
