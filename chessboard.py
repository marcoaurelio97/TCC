import numpy as np
from functions import *


class Chessboard:
    board = np.array([])
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    pieces = 'rnbkqpRNBQKP'

    def __init__(self):
        self.initial_state()

    def initial_state(self):
        self.board = np.array([
            ['r', 'n', 'b', 'k', 'q', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ])

    def print_board(self):
        # cls()
        count = 0
        for y in range(8):
            line = str(count) + '  '
            count += 1
            for x in range(8):
                line += ' ' + self.board[y][x]
            print(line)
        print('\n    A B C D E F G H\n')

    def move(self, x_curr, y_curr, x_next, y_next):
        x_curr = self.letters.index(x_curr)
        x_next = self.letters.index(x_next)

        # if not self.validate_moviment(x_curr, y_curr):
        #     return False
        # elif self.get_moves(x_curr, y_curr):
        #     return False

        self.board[int(y_next)][int(x_next)] = self.board[int(y_curr)][int(x_curr)]
        self.board[int(y_curr)][int(x_curr)] = '.'

        return True

    def validate_moviment(self, x, y):
        piece = self.board[int(y)][int(x)]

        if self.pieces.find(piece) == -1:
            return False

        return True

    def get_moves(self, piece, x, y):
        piece = piece.upper()
        moves = []

        if piece == 'P':
            moves.append((x+1, y))
            print(moves)
        elif piece == 'R':
            print('aaaaa')
        elif piece == 'N':
            a = 1
            # potential_moves += [(x + 2, y + 1), (x + 2, y - 1)
            #     , (x + 1, y + 2), (x + 1, y - 2)
            #     , (x - 2, y - 1), (x - 2, y + 1)
            #     , (x - 1, y + 2), (x - 1, y - 2)]
        elif piece == 'B':
            print('aaaaa')
        elif piece == 'K':
            print('aaaaa')
        elif piece == 'Q':
            print('aaaaa')
        else:
            return False
