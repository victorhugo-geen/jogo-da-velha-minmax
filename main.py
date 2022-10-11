from jogo_da_velha import criarBoard, fazMovimento, getInputValido, \
    printBoard, verificaGanhador, verificaMovimento

from minimax import movimentoIA
# jogador = 1 para jogar
jogador = 0
board = criarBoard()
ganhador = False
while not ganhador:
    printBoard(board)
    print("===================")
    if jogador == 0:
        i, j = movimentoIA(board, jogador)
    else:
        i = getInputValido("Digite a linha: ")
        j = getInputValido("Digite a coluna: ")

    # Verifica se o movimento é valido, faz a jogada e alterna o jogador
    if verificaMovimento(board, i, j):
        fazMovimento(board, i, j, jogador)
        jogador = (jogador + 1) % 2
    else:
        print("A posicao informada ja está ocupada")

    ganhador = verificaGanhador(board)

print("===================")
printBoard(board)
print("Resultado = ", ganhador)
print("===================")
