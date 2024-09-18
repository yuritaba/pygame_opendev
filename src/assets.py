"""
Módulo que gerencia os assets do jogo Castelo Assombrado.

Este módulo contém a função `load_assets`, que carrega e organiza todos os 
recursos gráficos e sonoros necessários para o funcionamento do jogo, como
imagens, animações e sons. Os assets são carregados uma vez e armazenados em
um dicionário para fácil acesso durante o jogo.
"""

import os
import pygame
from config import BOTAO_HEIGHT,BOTAO_WIDTH,HEIGHT,IMG_DIR,SND_DIR,PERSONAGEM_WIDTH,MONSTRO_WIDTH, \
    PERSONAGEM_HEIGHT,MONSTRO_HEIGHT,WIDTH,BLACKOUT_WIDTH,BLACKOUT_HEIGHT,CHAVE_WIDTH,CHAVE_HEIGHT

SWOOSH_SOUND =  'swoosh_sound'
BACKGROUND = 'background'
BOTAO_JOGAR  = 'jogar'
PERSONAGEM_PRINCIPAL = 'personagem_principal'
MONSTRO = 'monstro'
MONSTRO2 = 'monstro2'
MONSTRO3 = 'monstro3'
MONSTRO4 = 'monstro4'
MONSTRO5 = 'monstro5'
CHAO_CASTELO = 'chao_castelo'
PAREDE = 'parede'
PAREDE2 = 'parede2'
PAREDE3 = 'parede3'
PAREDE4 = 'parede4'
PAREDE5 = 'parede5'
PAREDE6 = 'parede6'
ANIMACAO_DIREITA = 'animacao_direita'
ANIMACAO_ESQUERDA = 'animacao_esquerda'
PARADO=  'parado'
PLAYER=  'player'
BLACKOUT = 'blackout'
CHAVE = 'chave'
VITORIA_BG='vitoria_bg'
PORTA = 'porta'
BOTAO_JOGARN = 'jogar_novamente'
BOTAO_JOGARN2 = 'jogar_novamente2'
ALCAPAS='alcapas'
RAIO='raio'

def load_images(assets):
    "Função que carrega as imagens e as retorna no dicionário assets"
    #imagens
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'castelo.png')).convert()
    assets[BACKGROUND] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))
    assets[BOTAO_JOGAR] = pygame.image.load(os.path.join(IMG_DIR,'botao_jogar.png')).convert_alpha()
    assets[BOTAO_JOGAR] = pygame.transform.scale(assets[BOTAO_JOGAR], (BOTAO_WIDTH, BOTAO_HEIGHT))
    assets[MONSTRO] = pygame.image.load(os.path.join(IMG_DIR, 'monstro.png')).convert_alpha()
    assets[MONSTRO] = pygame.transform.scale(assets[MONSTRO], (MONSTRO_WIDTH, MONSTRO_HEIGHT))
    assets[MONSTRO2] = pygame.image.load(os.path.join(IMG_DIR, 'Monstro2.png')).convert_alpha()
    assets[MONSTRO2] = pygame.transform.scale(assets[MONSTRO2], (MONSTRO_WIDTH, MONSTRO_HEIGHT))
    assets[MONSTRO3] = pygame.image.load(os.path.join(IMG_DIR, 'Monstro3.png')).convert_alpha()
    assets[MONSTRO3] = pygame.transform.scale(assets[MONSTRO3], (MONSTRO_WIDTH, MONSTRO_HEIGHT))
    assets[MONSTRO4] = pygame.image.load(os.path.join(IMG_DIR, 'Monstro4.png')).convert_alpha()
    assets[MONSTRO4] = pygame.transform.scale(assets[MONSTRO4], (MONSTRO_WIDTH, MONSTRO_HEIGHT))
    assets[MONSTRO5] = pygame.image.load(os.path.join(IMG_DIR, 'Monstro5.png')).convert_alpha()
    assets[MONSTRO5] = pygame.transform.scale(assets[MONSTRO5], (MONSTRO_WIDTH, MONSTRO_HEIGHT))
    assets[CHAO_CASTELO] = pygame.image.load(os.path.join(IMG_DIR, 'chao_castelo.png')).convert()
    assets[CHAO_CASTELO] = pygame.transform.scale(assets[CHAO_CASTELO], (WIDTH, HEIGHT))
    assets[BLACKOUT] = pygame.image.load(os.path.join(IMG_DIR, 'Blackout.png')).convert_alpha()
    assets[BLACKOUT] = pygame.transform.scale(assets[BLACKOUT], (BLACKOUT_WIDTH, BLACKOUT_HEIGHT))
    assets[CHAVE] = pygame.image.load(os.path.join(IMG_DIR, 'chave.png')).convert_alpha()
    assets[CHAVE] = pygame.transform.scale(assets[CHAVE], (CHAVE_WIDTH, CHAVE_HEIGHT))
    assets[VITORIA_BG] = pygame.image.load(os.path.join(IMG_DIR, 'Vitoria.png')).convert()
    assets[VITORIA_BG] = pygame.transform.scale(assets[VITORIA_BG], (WIDTH, HEIGHT))
    assets[PORTA] = pygame.image.load(os.path.join(IMG_DIR, 'porta.png')).convert_alpha()
    assets[BOTAO_JOGARN] = pygame.image.load(os.path.join(IMG_DIR, \
                                                           'botao_jogar_n.png')).convert_alpha()
    assets[BOTAO_JOGARN] = pygame.transform.scale(assets[BOTAO_JOGARN], (BOTAO_WIDTH, BOTAO_HEIGHT))
    assets[BOTAO_JOGARN2] = pygame.image.load(os.path.join(IMG_DIR, \
                                                            'botao_jogar_n2.png')).convert_alpha()
    assets[BOTAO_JOGARN2] = pygame.transform.scale(assets[BOTAO_JOGARN2], \
                                                    (BOTAO_WIDTH, BOTAO_HEIGHT))
    assets[ALCAPAS] = pygame.image.load(os.path.join(IMG_DIR, 'alcapas.png')).convert_alpha()
    assets[ALCAPAS] = pygame.transform.scale(assets[ALCAPAS], (40, 40))
    assets[RAIO] = pygame.image.load(os.path.join(IMG_DIR, 'raio.png')).convert_alpha()
    assets[RAIO] = pygame.transform.scale(assets[RAIO], (40, 40))
    return assets

def load_assets():
    "Função que carrega os assets do jogo"
    assets = {}
    assets = load_images(assets)

    #Estados do personagem

    assets[PARADO] = pygame.image.load(os.path.join(IMG_DIR, 'parado.png')).convert_alpha()
    assets[PARADO] = pygame.transform.scale(assets[PARADO], (PERSONAGEM_WIDTH, PERSONAGEM_HEIGHT))

        #animação de andar
    animacao_direita = []
    for i in range(8):
        # Os arquivos de animação são numerados de 00 a 08
        filename = os.path.join(IMG_DIR, f'{i}.png')
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (PERSONAGEM_WIDTH, PERSONAGEM_HEIGHT))
        animacao_direita.append(img)
    assets[ANIMACAO_DIREITA] = animacao_direita

    animacao_esquerda = []
    for i in range(8):
        # Os arquivos de animação são numerados de 00 a 08
        filename = os.path.join(IMG_DIR, f'esquerda{i}.png')
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (PERSONAGEM_WIDTH, PERSONAGEM_HEIGHT))
        animacao_esquerda.append(img)
    assets[ANIMACAO_ESQUERDA] = animacao_esquerda

    #Paredes
    assets[PAREDE] = pygame.image.load(os.path.join(IMG_DIR, 'Parede.png')).convert()
    assets[PAREDE] = pygame.transform.scale(assets[PAREDE], (40, 40))
    assets[PAREDE2] = pygame.image.load(os.path.join(IMG_DIR, 'Parede2.png')).convert()
    assets[PAREDE2] = pygame.transform.scale(assets[PAREDE2], (40, 40))
    assets[PAREDE3] = pygame.image.load(os.path.join(IMG_DIR, 'Parede3.png')).convert()
    assets[PAREDE3] = pygame.transform.scale(assets[PAREDE3], (40, 40))
    assets[PAREDE4] = pygame.image.load(os.path.join(IMG_DIR, 'Parede4.png')).convert()
    assets[PAREDE4] = pygame.transform.scale(assets[PAREDE4], (40, 40))
    assets[PAREDE5] = pygame.image.load(os.path.join(IMG_DIR, 'Parede5.png')).convert()
    assets[PAREDE5] = pygame.transform.scale(assets[PAREDE5], (40, 40))
    assets[PAREDE6] = pygame.image.load(os.path.join(IMG_DIR, 'Parede6.png')).convert()
    assets[PAREDE6] = pygame.transform.scale(assets[PAREDE6], (40, 40))

    #sons
    pygame.mixer.music.load(os.path.join(SND_DIR, 'soundtrack.mp3'))
    pygame.mixer.music.set_volume(0.9)
    assets[SWOOSH_SOUND]= pygame.mixer.Sound(os.path.join(SND_DIR, 'swoosh_de_terror.wav'))

    return assets
