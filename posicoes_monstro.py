"""
Módulo que define os movimentos dos monstros no jogo Castelo Assombrado.

Contém funções para adicionar movimentos em listas específicas que representam
os caminhos que cada monstro seguirá no jogo.
"""

lista_mov=[]
lista_mov2=[]
lista_mov3=[]
lista_mov4=[]
lista_mov5=[]

def monstro_esquerda(lista):
    """Adiciona movimentos para a esquerda na lista."""
    for _ in range(40):
        lista.append([-1, 0])
    return lista

def monstro_baixo(lista):
    """Adiciona movimentos para baixo na lista."""
    for _ in range(40):
        lista.append([0, 1])
    return lista

def monstro_cima(lista):
    """Adiciona movimentos para cima na lista."""
    for _ in range(40):
        lista.append([0, -1])
    return lista

def monstro_direita(lista):
    """Adiciona movimentos para a direita na lista."""
    for _ in range(40):
        lista.append([1, 0])
    return lista



for i in range(2):
    monstro_direita(lista_mov)

for i in range(2):
    monstro_baixo(lista_mov)

for i in range(2):
    monstro_esquerda(lista_mov)

for i in range(2):
    monstro_baixo(lista_mov)

for i in range(2):
    monstro_esquerda(lista_mov)

for i in range(2):
    monstro_baixo(lista_mov)

for i in range(2):
    monstro_esquerda(lista_mov)

for i in range(2):
    monstro_baixo(lista_mov)

for i in range(3):
    monstro_esquerda(lista_mov)

for i in range(4):
    monstro_baixo(lista_mov)

for i in range(2):
    monstro_esquerda(lista_mov)

for i in range(3):
    monstro_cima(lista_mov)

for i in range(2):
    monstro_esquerda(lista_mov)

for i in range(3):
    monstro_cima(lista_mov)

for i in range(2):
    monstro_esquerda(lista_mov)

for i in range(6):
    monstro_cima(lista_mov)

for i in range(2):
    monstro_direita(lista_mov)

for i in range(4):
    monstro_baixo(lista_mov)

for i in range(8):
    monstro_direita(lista_mov)

for i in range(2):
    monstro_cima(lista_mov)

for i in range(5):
    monstro_direita(lista_mov)

for i in range(2):
    monstro_cima(lista_mov)

for i in range(2):
    monstro_esquerda(lista_mov)

###monstro 2###

for i in range(8):
    monstro_esquerda(lista_mov2)

for i in range(4):
    monstro_baixo(lista_mov2)

for i in range(2):
    monstro_direita(lista_mov2)

for i in range(2):
    monstro_baixo(lista_mov2)

for i in range(2):
    monstro_direita(lista_mov2)

for i in range(2):
    monstro_cima(lista_mov2)

for i in range(2):
    monstro_direita(lista_mov2)

for i in range(3):
    monstro_baixo(lista_mov2)

for i in range(2):
    monstro_direita(lista_mov2)

for i in range(5):
    monstro_cima(lista_mov2)


for i in range(5):
    monstro_baixo(lista_mov2)

for i in range(2):
    monstro_esquerda(lista_mov2)

for i in range(3):
    monstro_cima(lista_mov2)

for i in range(2):
    monstro_esquerda(lista_mov2)

for i in range(2):
    monstro_baixo(lista_mov2)

for i in range(2):
    monstro_esquerda(lista_mov2)

for i in range(2):
    monstro_cima(lista_mov2)

for i in range(2):
    monstro_esquerda(lista_mov2)

for i in range(4):
    monstro_cima(lista_mov2)

for i in range(8):
    monstro_direita(lista_mov2)



###monstro 3###

for i in range(3):
    monstro_baixo(lista_mov3)

for i in range(27):
    monstro_esquerda(lista_mov3)

for i in range(6):
    monstro_cima(lista_mov3)

for i in range(7):
    monstro_direita(lista_mov3)

for i in range(7):
    monstro_esquerda(lista_mov3)

for i in range(6):
    monstro_baixo(lista_mov3)

for i in range(27):
    monstro_direita(lista_mov3)

for i in range(3):
    monstro_cima(lista_mov3)


###monstro 4###

for i in range(4):
    monstro_esquerda(lista_mov4)

for i in range(2):
    monstro_cima(lista_mov4)

for i in range(3):
    monstro_direita(lista_mov4)

for i in range(2):
    monstro_cima(lista_mov4)

for i in range(5):
    monstro_direita(lista_mov4)

for i in range(4):
    monstro_baixo(lista_mov4)

for i in range(7):
    monstro_direita(lista_mov4)

for i in range(2):
    monstro_baixo(lista_mov4)

for i in range(15):
    monstro_esquerda(lista_mov4)

for i in range(2):
    monstro_cima(lista_mov4)

for i in range(4):
    monstro_direita(lista_mov4)

###monstro 5###

for i in range(5):
    monstro_esquerda(lista_mov5)

for i in range(4):
    monstro_baixo(lista_mov5)

for i in range(4):
    monstro_esquerda(lista_mov5)

for i in range(4):
    monstro_cima(lista_mov5)

for i in range(2):
    monstro_esquerda(lista_mov5)

for i in range(2):
    monstro_direita(lista_mov5)

for i in range(4):
    monstro_baixo(lista_mov5)

for i in range(4):
    monstro_direita(lista_mov5)

for i in range(4):
    monstro_cima(lista_mov5)

for i in range(5):
    monstro_direita(lista_mov5)
