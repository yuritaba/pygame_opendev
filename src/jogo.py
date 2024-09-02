"""
Módulo principal do jogo Castelo Assombrado.

Este módulo inicializa o jogo e gerencia a troca de estados entre as telas iniciais,
de jogo, vitória e reinício.
"""

import pygame
from config import WIDTH, HEIGHT, INIT, GAME, QUIT, VITORIA, MORTE
from init_screen import init_screen
from game_screen import game_screen
from vitoria_screen import vitoria_screen
from jogar_novamente_screen import jogar_novamente_screen

# Inicializa módulos do pygame
pygame.init()  # pylint: disable=no-member
pygame.mixer.init()  # pylint: disable=no-member

# Configura a janela do jogo
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Castelo Assombrado')

def main():
    """Função principal do jogo."""
    state = INIT
    while state != QUIT:
        if state == INIT:
            state = init_screen(window)
        elif state == GAME:
            state = game_screen(window)
        elif state == VITORIA:
            state = vitoria_screen(window)
        elif state == MORTE:
            state = jogar_novamente_screen(window)
        else:
            state = QUIT

    pygame.quit()  # pylint: disable=no-member

if __name__ == "__main__":
    main()
