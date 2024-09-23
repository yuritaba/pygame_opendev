"""Módulo para inicializar a tela de jogo com pygame e gerenciar a interface do usuário."""

import pygame
from config import BLACK, WIDTH, HEIGHT, GAME, QUIT
from assets import BACKGROUND, BOTAO_JOGAR, load_assets
from sprites import Button

def init_screen(window):
    """Inicializa a tela do jogo carregando recursos e preparando o ambiente gráfico."""
    assets = load_assets()

    background = assets[BACKGROUND]
    background_rect = background.get_rect()

    img_botao = assets[BOTAO_JOGAR]
    botao = Button(WIDTH // 2 - 224, HEIGHT // 2 + 15, img_botao, 0.5)

    pygame.mixer.music.play(loops=-1)
    running = True
    state = None
    while running:
        window.fill(BLACK)
        window.blit(background, background_rect)
        botao.draw(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if botao.press():  # Ajustado conforme a definição do método ‘press’
                    state = GAME
                    running = False

        pygame.display.flip()

    return state
