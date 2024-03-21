"""
Saber quantos LEDs vamos usar para montar determinado número;
Ex.: para formar o 3 são 5 LED '∃'

"""


def count_leds(evento: str):
    leds = {"0": 6, "1": 2, "2": 5, "3": 5, "4": 4, "5": 5, "6": 6, "7": 3, "8": 7, "9": 6}

    return leds[evento]


num = int(input("Digite: ").strip())

digitos = sum([count_leds(digito) for digito in str(num)])
print(digitos)

# digitos = [int(digito) for digito in str(num)] # Para gerar uma lista de inteiros
