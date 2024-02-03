# ######################### configurações inicias ###########################
import pygame
import random

pygame.init()
pygame.display.set_caption("Jogo Snake Python")
largura, altura = 1200, 800
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

#  cores RGB
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

# parametro da cobrinha 10px de largura e de altura
tamanho_quadrado = 20
velocidade_jogo = 15



def gerar_comidada():
    # para o quadrado da comida não ficar fora da tela e /20 depois * 20 para garantir que o quadrado
    # estará alinhado com a cobra
    comida_x = round(random.randrange(0, largura, tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura, tamanho_quadrado) / 20.0) * 20.0
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_Y):
    pygame.draw.rect(tela, verde, [comida_x, comida_Y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:                # x          y
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])  # pegar a posição de cada pixel

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvatica", 35)
    texto = fonte.render(f"Pontos: {pontuacao} ", True, vermelha)  # usando o 'True' o texto fica boleado
    tela.blit(texto,  [1, 1])
    return pontuacao



direcao = []
def selecionar_velocidade(tecla):
    # deslocamento da cobrinha
    nome_tecla = pygame.key.name(tecla)

    direcao.append(nome_tecla)


    if tecla == pygame.K_DOWN and direcao[0] != 'up':

        valocidade_x = 0
        velocidade_y = tamanho_quadrado
        direcao.clear()
        direcao.insert(0, nome_tecla)
        direcao.insert(1, valocidade_x)
        direcao.insert(2, velocidade_y)


    elif tecla == pygame.K_UP and direcao[0] != 'down':
        valocidade_x = 0
        velocidade_y = - tamanho_quadrado
        direcao.clear()
        direcao.insert(0, nome_tecla)
        direcao.insert(1, valocidade_x)
        direcao.insert(2, velocidade_y)


    elif tecla == pygame.K_RIGHT and direcao[0] != 'left':
        valocidade_x = tamanho_quadrado
        velocidade_y = 0
        direcao.clear()
        direcao.insert(0, nome_tecla)
        direcao.insert(1, valocidade_x)
        direcao.insert(2, velocidade_y)

    elif tecla == pygame.K_LEFT and direcao[0] != 'right':
        valocidade_x = - tamanho_quadrado
        velocidade_y = 0
        direcao.clear()
        direcao.insert(0, nome_tecla)
        direcao.insert(1, valocidade_x)
        direcao.insert(2, velocidade_y)


    else:
        valocidade_x = direcao[1]
        velocidade_y = direcao[2]
    return valocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False
    # a cobrinha vai começar na posição central com velocidade 0, ou seja, parada
    x = largura / 2
    y = altura / 2

    velocidade_x = 0  # velocidade de direção
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []
    comida_x, comida_y = gerar_comidada()

    while not fim_jogo:
        tela.fill(preta)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                print("finalizou")
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        # atualizar a posição da cobra
        x += velocidade_x
        y += velocidade_y

        # desenha_comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        # limitacao nas paredes
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        # desenha_cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]   # se a quantidade de ítems na lista for maior que o tamanho da cobra

        # ferifica se a cobrinha bateu no próprio corpo
        for pixel in pixels[: -1]:  # lista inteira menos o último ítem, pois retira a cabeça
            if pixel == [x, y]:
                fim_jogo = True
        desenhar_cobra(tamanho_quadrado, pixels)

        # desenha pontos
        desenhar_pontuacao(tamanho_cobra-1)


        # atualizacao da tela
        pygame.display.update()

        # criar uma nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comidada()





        # if tamanho_cobra > 20:
        #     relogio.tick(velocidade_jogo+25)
        #     print(desenhar_pontuacao(pontuacao=velocidade_jogo))
        # elif tamanho_cobra > 15:
        #     relogio.tick(velocidade_jogo+15)
        #     print(desenhar_pontuacao(pontuacao=velocidade_jogo))
        #
        # elif tamanho_cobra > 10:
        #     relogio.tick(velocidade_jogo + 10)
        #     print(desenhar_pontuacao(pontuacao=velocidade_jogo))
        #
        # elif tamanho_cobra > 5:
        #     relogio.tick(velocidade_jogo+5)
        #     print(desenhar_pontuacao(pontuacao=velocidade_jogo))
        # else:

        relogio.tick(velocidade_jogo)


# ############################# criar um loop infinito #######################

# desenhar os objetos do jogo na tela
# pontuação
# cobrinha
# comida


# criar a logica de terminar o jogo
# o que  acontece:
# cobra bateu na parede
# cobra bateu na propria cobra

# pegar a interações do usuario
# fechau a tela
# apertou as teclas do teclado pra mover a cobra

rodar_jogo()