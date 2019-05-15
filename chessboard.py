import numpy as np
from movement_rules import *

EMPTY_STATE = '.'


class Chessboard:
    board = None
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    pieces = 'rnbkqpRNBQKP'

    def __init__(self):
        self.initial_state()

    def initial_state(self):
        self.board = np.array([
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'k', 'q', 'b', 'n', 'r']
        ])

    def print_board(self):
        count = 7
        for y in range(7, -1, -1):
            line = str(count) + '  '
            count -= 1
            for x in range(8):
                line += ' ' + self.board[y][x]
            print(line)
        print('\n    A B C D E F G H\n')

    def move(self, x_curr, y_curr, x_next, y_next):
        if x_curr not in self.letters or x_next not in self.letters:
            raise Exception('\nInvalid positions!\n')

        x_curr = Movement().letters.index(x_curr)
        x_next = Movement().letters.index(x_next)
        piece = self.board[y_curr][x_curr]

        if Movement().verify_false_coordinates(x_curr, y_curr, x_next, y_next):
            raise Exception('\nInvalid movement!\n')

        if Movement().verify_piece_not_exists(self.board, x_curr, y_curr):
            raise Exception('\nInvalid movement!\n')

        moves = Movement().get_moves(self.board, piece, x_curr, y_curr)

        if [y_next, x_next] not in moves:
            raise Exception('\nInvalid movement!\n')

        piece = Movement().verify_pawn_promotion(piece, y_next)

        self.board[y_next][x_next] = piece
        self.board[y_curr][x_curr] = EMPTY_STATE
