import numpy as np
from functions import *

EMPTY_STATE = '.'


class Chessboard:
    board = np.array([])
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
        # cls()
        count = 7
        for y in range(7, -1, -1):
            line = str(count) + '  '
            count -= 1
            for x in range(8):
                line += ' ' + self.board[y][x]
            print(line)
        print('\n    A B C D E F G H\n')

    def move(self, x_curr, y_curr, x_next, y_next):
        x_curr = self.letters.index(x_curr)
        x_next = self.letters.index(x_next)
        piece = self.board[y_curr][x_curr]

        if self.verify_piece_not_exists(x_curr, y_curr):
            raise Exception('\nInvalid moviment!\n')

        moves = self.get_moves(piece, x_curr, y_curr)
        print(moves)

        if [y_next, x_next] not in moves:
            raise Exception('\nInvalid moviment!\n')

        self.board[y_next][x_next] = piece
        self.board[y_curr][x_curr] = EMPTY_STATE

    def verify_piece_not_exists(self, x, y):
        piece = self.board[y][x]

        if self.pieces.find(piece) == -1:
            return True

        return False

    def get_moves(self, piece, x, y):
        moves = []
        piece_upper = piece.upper()

        if piece_upper == 'P':
            if piece == 'P':
                moves.append([y + 1, x])

                if y == 1:
                    moves.append([y + 2, x])
                if y < 7 and x < 7 and self.board[y + 1][x + 1] != EMPTY_STATE:
                    moves.append([y + 1, x + 1])
                if y < 7 and x < 7 and self.board[y + 1][x - 1] != EMPTY_STATE:
                    moves.append([y + 1, x - 1])
            else:
                moves.append([y - 1, x])

                if y == 6:
                    moves.append([y - 2, x])
                if y > 0 and x > 0 and self.board[y - 1][x - 1] != EMPTY_STATE:
                    moves.append([y - 1, x - 1])
                if y > 0 and x > 0 and self.board[y - 1][x + 1] != EMPTY_STATE:
                    moves.append([y - 1, x + 1])
        elif piece_upper == 'R':
            for i in range(8):
                if 0 <= y + i < 8 and 0 <= x < 8 and not self.verify_piece_not_exists(x, y + i)\
                        and [y + i, x] not in moves and self.board[y + i][x] != piece:
                    moves.append([y + i, x])
                if 0 <= y - i < 8 and 0 <= x < 8 and not self.verify_piece_not_exists(x, y - i)\
                        and [y - i, x] not in moves and self.board[y - i][x] != piece:
                    moves.append([y - i, x])
                if 0 <= y < 8 and 0 <= x + i < 8 and not self.verify_piece_not_exists(x + i, y)\
                        and [y, x + i] not in moves and self.board[y][x + i] != piece:
                    moves.append([y, x + i])
                if 0 <= y < 8 and 0 <= x - i < 8 and not self.verify_piece_not_exists(x - i, y)\
                        and [y, x - i] not in moves and self.board[y][x - i] != piece:
                    moves.append([y, x - i])
        elif piece_upper == 'N':
            moves.append([y + 1, x + 2])
            moves.append([y - 1, x + 2])
            moves.append([y + 2, x + 1])
            moves.append([y - 2, x + 1])
            moves.append([y - 1, x - 2])
            moves.append([y + 1, x - 2])
            moves.append([y + 2, x - 1])
            moves.append([y - 2, x - 1])
        elif piece_upper == 'B':
            print('aaaaa')
        elif piece_upper == 'K':
            print('aaaaa')
        elif piece_upper == 'Q':
            print('aaaaa')

        return moves
