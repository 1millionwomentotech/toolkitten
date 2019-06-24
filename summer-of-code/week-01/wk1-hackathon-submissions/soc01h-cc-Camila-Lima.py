
L = 'terra'
W = 'agua'


def cont_blocks_processed(continent, x, y):
    # Para definir a posição, vamos usar as coordenadas x (horizontal) e y (vertical).

    # Se o bloco analisado não for de TERRA, ele não será contado.
    if continent[x][y] != L:
        return 0

    # Caso for de TERRA, ele será computado na contagem.
    blocks_processed = 1

    # Como o bloco atual já foi computado, ele será marcado como CONTADO. Desse modo,
    # não será considerado na próxima contagem.
    continent[x][y] = 'block_processed'

    # São verificadas todas as posições adjacentes ao bloco escolhido. Portanto, variando
    # as coordenadas x e y em 1, 0 e -1.
    # Este código é recursivo. Portanto, todas as posições serão testadas, uma a uma.
    blocks_processed = blocks_processed + cont_blocks_processed(continent, x - 1, y - 1)
    blocks_processed = blocks_processed + cont_blocks_processed(continent, x - 1, y)
    blocks_processed = blocks_processed + cont_blocks_processed(continent, x - 1, y + 1)

    blocks_processed = blocks_processed + cont_blocks_processed(continent, x, y - 1)
    blocks_processed = blocks_processed + cont_blocks_processed(continent, x, y + 1)

    blocks_processed = blocks_processed + cont_blocks_processed(continent, x + 1, y - 1)
    blocks_processed = blocks_processed + cont_blocks_processed(continent, x + 1, y)
    blocks_processed = blocks_processed + cont_blocks_processed(continent, x + 1, y + 1)

    # O retorno da função é a contagem dos blocos.
    return blocks_processed
