# Code Organization

O código do jogo "Castelo Assombrado" é organizado em vários módulos para manter a funcionalidade bem estruturada e fácil de gerenciar. Abaixo, uma visão geral dos principais arquivos e suas responsabilidades:

## Estrutura dos Arquivos do src

- **`jogo.py`**: Arquivo principal que inicializa o jogo, gerencia os estados do jogo e controla a transição entre as telas (inicial, jogo, vitória e morte).

- **`assets.py`**: Gerencia os recursos do jogo, incluindo o carregamento de imagens, sons e animações. Utiliza um dicionário para armazenar os recursos para fácil acesso.

- **`sprites.py`**: Define as classes de sprites para personagens, monstros, paredes e outros elementos interativos do jogo. Cada classe gerencia a aparência e o comportamento dos sprites.

- **`game_screen.py`**: Define a lógica principal do jogo, incluindo movimentação do personagem, colisões, coleta de chaves e interação com monstros.

- **`vitoria_screen.py`**: Gerencia a tela de vitória, exibida quando o jogador coleta todas as chaves e escapa do castelo.

- **`scene.py`**: Responsável por criar e organizar as paredes e outras estruturas no cenário do jogo.

- **`posicoes_chave.py`**: Define as posições iniciais das chaves no mapa, com posições geradas aleatoriamente para cada partida.

- **`posicoes_monstro.py`**: Define os movimentos e padrões de comportamento dos monstros no jogo.

- **`init_screen.py`**: Gerencia a tela inicial do jogo, exibindo o menu principal onde o jogador pode iniciar o jogo. Inclui a lógica para exibir e interagir com os botões da interface de início.

- **`mapa.py`**: Contém a definição da matriz do mapa, incluindo as posições das paredes, monstros, e outros elementos do cenário. Este arquivo organiza o layout do castelo onde o jogo acontece.

- **`config.py`**: Define configurações e constantes usadas em todo o jogo, como dimensões da tela, caminhos para os diretórios de recursos, cores, e outras constantes de configuração que facilitam a manutenção do código.

- **`jogar_novamente_screen.py`**: Gerencia a tela de “Jogar Novamente”, exibida quando o jogador perde o jogo. Permite ao jogador reiniciar a partida ou sair do jogo, com botões que controlam essas opções.

## Estrutura de Pastas

- **`src/assets/`**: Contém todas as imagens, sons e outros recursos gráficos do jogo.
- **`docs/`**: Pasta criada para o site da documentação usando MkDocs.

## Fluxo do Jogo

1. O jogo começa na tela inicial onde o jogador clica em "Jogar".
2. Na tela principal do jogo, o personagem deve coletar 4 chaves enquanto evita monstros.
3. Após coletar todas as chaves, o jogador deve chegar à porta para vencer o jogo.
4. Caso o personagem encoste em um monstro, ele morre e o jogo termina, com a opção de reiniciar.