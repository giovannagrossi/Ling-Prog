import numpy as np
import numpy.random as npr

# Em uma matriz (5x5), qual é o índice do elemento 10? 

print(np.unravel_index(10, (5,5)))


# Em uma matriz (5x5), qual é o índice do elemento 42? 

print(np.unravel_index(42, (5,5,5)))


# Tabuleiro de xadrez em matriz (par = brancas, impar = pretas)

chess_board = np.zeros((8,8))
chess_board[1::2, ::2] = 1
chess_board[::2, 1::2] = 1


print(chess_board)





