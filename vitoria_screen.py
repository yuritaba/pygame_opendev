"""
Módulo que define a tela de vitória no jogo Castelo Assombrado.

Esta função gerencia a lógica e a renderização da tela de vitória,
permitindo ao jogador interagir com elementos como botões e o personagem principal.
"""

import pygame
from assets import load_assets, BOTAO_JOGARN, PARADO, ANIMACAO_DIREITA, ANIMACAO_ESQUERDA
from sprites import Personagem, Button
from config import HEIGHT, WIDTH, FPS, QUIT, GAME, YELLOW
from mapa import matriz2
from scene import make

def vitoria_screen(window):
    """
    Função que exibe a tela de vitória do jogo e permite interação com botões
    e movimento do personagem principal.

    Args:
        window: A janela do jogo onde a tela será desenhada.

    Returns:
        state: O estado do jogo após a execução da tela de vitória.
    """
    clock = pygame.time.Clock()
    assets = load_assets()
    all_sprites = pygame.sprite.Group()
    all_walls = make(matriz2)

    personagem_principal = Personagem(575, 562, assets[PARADO], all_walls)
    all_sprites.add(personagem_principal)

    esq_pressionado = False  # usado na animação
    dir_pressionado = False  # usado na animação

    img_botao = assets[BOTAO_JOGARN]
    botao = Button(WIDTH / 2 - 225, HEIGHT / 2 - 125, img_botao, 0.5)

    for wall in all_walls.sprites():
        all_sprites.add(wall)

    running = True
    state = QUIT # pylint: disable=E1101

    while running:
        clock.tick(FPS)
        window.fill(YELLOW)
        botao.draw(window)

        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT: # pylint: disable=E1101
                running = False

            if botao.press():
                state = GAME
                running = False

            if event.type == pygame.KEYDOWN: # pylint: disable=E1101
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_RIGHT: # pylint: disable=E1101
                    personagem_principal.speedx += 1
                    dir_pressionado = True  # animação de andar para direita

                if event.key == pygame.K_UP: # pylint: disable=E1101
                    personagem_principal.speedy -= 1
                    dir_pressionado = True  # animação de andar para direita

                if event.key == pygame.K_DOWN: # pylint: disable=E1101
                    personagem_principal.speedy += 1
                    dir_pressionado = True  # animação de andar para direita

                if event.key == pygame.K_LEFT: # pylint: disable=E1101
                    personagem_principal.speedx -= 1
                    esq_pressionado = True

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP: # pylint: disable=E1101
                if event.key == pygame.K_LEFT: # pylint: disable=E1101
                    personagem_principal.speedx = 0
                    esq_pressionado = False
                    personagem_principal.parar(assets[PARADO])

                if event.key == pygame.K_RIGHT: # pylint: disable=E1101
                    personagem_principal.speedx = 0
                    dir_pressionado = False
                    personagem_principal.parar(assets[PARADO])

                if event.key == pygame.K_UP: # pylint: disable=E1101
                    dir_pressionado = False
                    personagem_principal.parar(assets[PARADO])
                    personagem_principal.speedy = 0

                if event.key == pygame.K_DOWN: # pylint: disable=E1101
                    dir_pressionado = False
                    personagem_principal.parar(assets[PARADO])
                    personagem_principal.speedy = 0

        if esq_pressionado:
            personagem_principal.esquerdo(assets[ANIMACAO_ESQUERDA])

        if dir_pressionado:
            personagem_principal.direita(assets[ANIMACAO_DIREITA])

        all_sprites.update(personagem_principal)  # atualiza a posição do personagem

        all_sprites.draw(window)
        pygame.display.flip()

    return state
