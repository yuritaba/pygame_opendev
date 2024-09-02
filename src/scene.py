"""
Módulo que cria as cenas do jogo Castelo Assombrado.

Este módulo utiliza matrizes para gerar grupos de paredes nas posições corretas
usando diferentes tipos de paredes definidas nos assets.
"""

import pygame
from assets import PAREDE2, load_assets, PAREDE, PAREDE3, PAREDE4, PAREDE5, PAREDE6
from sprites import Wall

def make(matrix):
    """Cria as paredes do jogo com base na matriz fornecida."""
    assets = load_assets()
    all_walls = pygame.sprite.Group()
    for row_index, row in enumerate(matrix):
        for col_index, cell in enumerate(row):
            x_coord = row_index * 40
            y_coord = col_index * 40
            if cell == 1:
                img_parede = assets[PAREDE]
                all_walls.add(Wall(img_parede, x_coord, y_coord))  # Wall é a classe das paredes
            elif cell == 2:
                img_parede = assets[PAREDE2]
                all_walls.add(Wall(img_parede, x_coord, y_coord))
            elif cell == 3:
                img_parede = assets[PAREDE3]
                all_walls.add(Wall(img_parede, x_coord, y_coord))
            elif cell == 4:
                img_parede = assets[PAREDE4]
                all_walls.add(Wall(img_parede, x_coord, y_coord))
            elif cell == 5:
                img_parede = assets[PAREDE5]
                all_walls.add(Wall(img_parede, x_coord, y_coord))
            elif cell == 6:
                img_parede = assets[PAREDE6]
                all_walls.add(Wall(img_parede, x_coord, y_coord))
    return all_walls
