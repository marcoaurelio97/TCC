EMPTY_STATE = '.'

from movement_rules import Movement
import random


class Minimax:

    @staticmethod
    def get_minimax_move(chessboard):
        moves = Movement.get_best_move(chessboard.board)

        return random.choice(moves)

    @staticmethod
    def get_best_move(board):
        moves = []

        for y in range(0, 8):
            for x in range(0, 8):
                if board[y][x] != EMPTY_STATE and board[y][x].islower():
                    iteration_moves = Movement.get_moves(board, board[y][x], x, y)
                    for k in iteration_moves:
                        moves.append([y, Movement.letters[x], k[0], Movement.letters[k[1]]])

        return moves

    #https://github.com/Cledersonbc/tic-tac-toe-minimax/blob/master/py_version/minimax.py