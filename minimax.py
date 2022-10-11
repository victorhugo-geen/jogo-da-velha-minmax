from jogo_da_velha import branco, token, verificaGanhador


def movimentoIA(board, jogador):
    # Pega e itera sobre as possibilidades de jogada
    possibilidades = getPosicoes(board)
    melhor_valor = None
    melhor_movimento = None
    for possibilidade in possibilidades:
        # Para cada possibilidade da próxima jogada, chama o minimax para simular 
        # o resultado da partida e armazena esse resultado no valor
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = minimax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = branco

        # Na primeira iteração, define a primeira possibilidade como a mulher
        if melhor_valor is None:
            melhor_valor = valor
            melhor_movimento = possibilidade

        # Se o jogador for 0 (X), atribui como melhor valor a primeira possibilidade que ele ganhe 
        elif jogador == 0:
            if valor > melhor_valor:
                melhor_valor = valor
                melhor_movimento = possibilidade

        # E faz a mesma coisa caso o jogador seja 1 (O)
        elif jogador == 1:
            if valor < melhor_valor:
                melhor_valor = valor
                melhor_movimento = possibilidade

    # Retorna a linha e a coluna do melhor movimento encontrado
    return melhor_movimento[0], melhor_movimento[1]


def getPosicoes(board):
    posicoes = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == branco:
                posicoes.append([i, j])

    return posicoes


score = {
    "EMPATE": 0,
    "X": 1,
    "O": -1
}


def minimax(board, jogador):
    # se alguem ganhou, retorna o jogador ou o empate
    ganhador = verificaGanhador(board)
    if ganhador:
        return score[ganhador]

    # alterna entre 0 e 1
    jogador = (jogador + 1) % 2

    # Pega todas as possibilidades de jogada
    possibilidades = getPosicoes(board)
    # Reseta o melhor valor
    melhor_valor = None
    # Itera sobre as possibilidades
    for possibilidade in possibilidades:
        # Simula a jogada no espaço vazio atual
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        # Recebe o valor da jogada simulada
        valor = minimax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = branco

        # Na primeira iteração, atribui como melhor valor a primeira possibilidade
        if melhor_valor is None:
            melhor_valor = valor

        # Se o jogador for 0 (X), atribui como melhor valor a primeira possibilidade que ele ganhe 
        # (ou continua com a primeira caso não haja melhor possibilidade que ela)
        elif jogador == 0:
            if valor > melhor_valor:
                melhor_valor = valor
        # Faz a mesma coisa para o jogador 1 (O)
        elif jogador == 1:
            if valor < melhor_valor:
                melhor_valor = valor

    return melhor_valor
