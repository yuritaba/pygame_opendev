"""
Módulo que define a tela de jogo principal do Castelo Assombrado.

Este módulo contém a função `game_screen`, que gerencia a lógica e a renderização
da tela principal do jogo, incluindo a movimentação do personagem, monstros,
interação com itens e a verificação de condições de vitória ou derrota.
"""

from os import path
from random import randint
import pygame
from mapa import matriz
from config import BLACK, FPS, QUIT, VITORIA, IMG_DIR, MORTE
from assets import (
    ALCAPAS,
    ANIMACAO_DIREITA,
    ANIMACAO_ESQUERDA,
    BLACKOUT,
    CHAO_CASTELO,
    PARADO,
    RAIO,
    load_assets,
    CHAVE,
    PORTA,
)
from sprites import Alcapas, Blackout, Personagem, Monstro, Chave, Pontos, Porta, Raio
from scene import make
from posicoes_chave import posicoes, posicoes_clarao
from posicoes_monstro import lista_mov, lista_mov2, lista_mov3, lista_mov4, lista_mov5


def game_screen(window):
    """
    Game screen function, where the game logic is implemented.
    """
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()
    all_sprites = pygame.sprite.Group()
    all_chaves = pygame.sprite.Group()
    all_monstros = pygame.sprite.Group()
    all_personagem_principal = pygame.sprite.Group()
    all_blackout = pygame.sprite.Group()
    all_pontos_chaves = pygame.sprite.Group()
    all_porta = pygame.sprite.Group()
    all_alcapas1 = pygame.sprite.Group()
    all_alcapas2 = pygame.sprite.Group()
    all_raios = pygame.sprite.Group()
    times_list = [0] * 5
    movs_list = [lista_mov, lista_mov2, lista_mov3, lista_mov4, lista_mov5]

    background = pygame.image.load(path.join(IMG_DIR, "chao_castelo.png")).convert()
    background_rect = background.get_rect()
    personagem_principal = pygame.image.load(
        path.join(IMG_DIR, "parado.png")
    ).convert_alpha()

    all_walls = make(matriz)

    img_personagem_principal = assets[PARADO]
    personagem_principal = Personagem(575, 562, img_personagem_principal, all_walls)
    load_monstros(assets, all_walls, all_sprites, all_monstros)

    blackout = Blackout(575, 562, assets[BLACKOUT])

    porta = Porta(560, 0, assets[PORTA])

    all_sprites.add(porta)
    all_porta.add(porta)

    img_alcapas = assets[ALCAPAS]
    alcapas1 = Alcapas(200, 40, img_alcapas)
    alcapas2 = Alcapas(1040, 440, img_alcapas)

    all_alcapas1.add(alcapas1)
    all_alcapas2.add(alcapas2)

    all_sprites.add(alcapas1)
    all_sprites.add(alcapas2)

    reposicao_chave = []
    img_chave = assets[CHAVE]
    for i in range(4):
        chave = Chave(img_chave, posicoes)
        reposicao_chave.append([chave.x, chave.y])
        all_sprites.add(chave)
        all_chaves.add(chave)

    for i in range(4):
        posicoes.append(reposicao_chave[i])

    pos_raio = posicoes_clarao[randint(0, len(posicoes_clarao) - 1)]
    x_raio = pos_raio[0]
    y_raio = pos_raio[1]

    img_raio = assets[RAIO]
    raio = Raio(x_raio, y_raio, img_raio)

    all_raios.add(raio)
    all_sprites.add(raio)

    pontos = 0

    all_sprites.add(personagem_principal)
    all_personagem_principal.add(personagem_principal)

    all_sprites.add(blackout)
    all_blackout.add(blackout)

    # Esquerda, direita, cima, baixo
    pressed_keys = [False] * 4

    for s in all_walls.sprites():
        all_sprites.add(s)

    timer = 2 * FPS

    pygame.mixer.music.play(loops=-1)
    running = True
    state = MORTE
    while running:
        clock.tick(FPS)
        window.fill(BLACK)
        window.blit(assets[CHAO_CASTELO], background_rect)

        # se o monstro bater no personagem principal ele morre e acaba o jogo
        hits = pygame.sprite.spritecollide(personagem_principal, all_monstros, False)
        if hits != []:
            state = MORTE
            running = False

        hit = pygame.sprite.spritecollide(personagem_principal, all_chaves, True)
        if hit != []:
            pontos += 1

        hit2 = pygame.sprite.spritecollide(personagem_principal, all_porta, False)
        if hit2 != [] and pontos == 4:
            state = VITORIA
            running = False

        hit3 = pygame.sprite.spritecollide(personagem_principal, all_alcapas1, False)
        if hit3 != []:
            personagem_principal.rect.topleft = (1040, 400)

        hit4 = pygame.sprite.spritecollide(personagem_principal, all_alcapas2, False)
        if hit4 != []:
            personagem_principal.rect.topleft = (200, 80)

        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:  # pylint: disable=E1101
                state = QUIT
                running = False
            if event.type == pygame.KEYDOWN:  # pylint: disable=E1101
                on_keydown(event.key, personagem_principal, pressed_keys)

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                on_keyup(event.key, assets, personagem_principal, pressed_keys)

        for index, monstro in enumerate(all_monstros):
            monstro.andar(movs_list[index], times_list[index])

        for index, time in enumerate(times_list):
            if time + 1 >= len(movs_list[index]):
                times_list[index] = 0
            else:
                times_list[index] += 1

        control_animation(
            pressed_keys,
            personagem_principal,
            assets,
        )

        all_sprites.update(
            personagem_principal
        )  # atualiza a posição do personagem e do monstro

        all_sprites.draw(window)
        all_porta.draw(window)
        all_alcapas1.draw(window)
        all_alcapas2.draw(window)
        all_chaves.draw(window)

        hit5 = pygame.sprite.spritecollide(personagem_principal, all_raios, True)
        if len(hit5) > 0:
            timer = 0
        if timer >= 2 * FPS:
            all_blackout.draw(window)

        timer += 1

        all_personagem_principal.draw(window)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

        x = 10
        for i in range(pontos):
            ponto_chave = Pontos(img_chave, x, 570)
            all_pontos_chaves.add(ponto_chave)
            x += 40
        all_pontos_chaves.draw(window)

        pygame.display.update()  # Mostra o novo frame para o jogador
    return state


def control_animation(pressed_keys, personagem_principal: Personagem, assets):
    """
    Função que controla a animação do personagem principal.
    """
    esq_pressionado = pressed_keys[0]
    dir_pressionado = pressed_keys[1]
    cima_pressionado = pressed_keys[2]
    baixo_pressionado = pressed_keys[3]
    if esq_pressionado and not dir_pressionado:
        personagem_principal.esquerdo(assets[ANIMACAO_ESQUERDA])

    if dir_pressionado:
        personagem_principal.direita(assets[ANIMACAO_DIREITA])

    if cima_pressionado and not esq_pressionado and not dir_pressionado:
        personagem_principal.direita(assets[ANIMACAO_DIREITA])

    if baixo_pressionado and not esq_pressionado and not dir_pressionado:
        personagem_principal.direita(assets[ANIMACAO_DIREITA])


def on_keyup(key, assets, main_character: Personagem, key_pressed):
    """
    Match the keyup event with the correct action.
    """
    if key == pygame.K_LEFT:  # pylint: disable=E1101
        main_character.speedx = 0
        key_pressed[0] = False
        main_character.parar(assets[PARADO])

    if key == pygame.K_RIGHT:  # pylint: disable=E1101
        main_character.speedx = 0
        key_pressed[1] = False
        main_character.parar(assets[PARADO])

    if key == pygame.K_UP:  # pylint: disable=E1101
        key_pressed[2] = False
        main_character.parar(assets[PARADO])
        main_character.speedy = 0

    if key == pygame.K_DOWN:  # pylint: disable=E1101
        key_pressed[3] = False
        main_character.parar(assets[PARADO])
        main_character.speedy = 0


def on_keydown(key, main_character: Personagem, key_pressed):
    """
    Match the keydown event with the correct action.
    """
    if key == pygame.K_LEFT:  # pylint: disable=E1101
        main_character.speedx -= 1
        key_pressed[0] = True
    elif key == pygame.K_RIGHT:  # pylint: disable=E1101
        main_character.speedx += 1
        key_pressed[1] = True  # animação de andar para direita
    elif key == pygame.K_UP:  # pylint: disable=E1101
        main_character.speedy -= 1
        key_pressed[2] = True  # animação de andar para direita
    elif key == pygame.K_DOWN:  # pylint: disable=E1101
        main_character.speedy += 1
        key_pressed[3] = True


def load_monstros(assets, all_walls, all_sprites, all_monstros):
    """
    Função que carrega as imagens dos monstros do jogo.
    """
    positions = [(565, 40), (1125, 40), (1125, 400), (445, 440), (485, 40)]
    for index, position in enumerate(positions):
        name = f"monstro{index + 1}" if index != 0 else "monstro"
        img_monstro = assets[name]
        monstro = Monstro(img_monstro, all_walls, *position)
        all_sprites.add(monstro)
        all_monstros.add(monstro)
