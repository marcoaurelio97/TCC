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

        if self.verify_false_coordinates(x_curr, y_curr, x_next, y_next):
            raise Exception('\nInvalid moviment!\n')

        if self.verify_piece_not_exists(x_curr, y_curr):
            raise Exception('\nInvalid moviment!\n')

        moves = self.get_moves(piece, x_curr, y_curr)

        if [y_next, x_next] not in moves:
            raise Exception('\nInvalid moviment!\n')

        self.board[y_next][x_next] = piece
        self.board[y_curr][x_curr] = EMPTY_STATE

    @staticmethod
    def verify_false_coordinates(x_curr, y_curr, x_next, y_next):
        r = range(0, 8)

        if x_curr not in r or y_curr not in r or x_next not in r or y_next not in r:
            return True

        return False

    def verify_piece_not_exists(self, x, y):
        piece = self.board[y][x]

        if self.pieces.find(piece) == -1:
            return True

        return False

    def get_moves(self, piece, x, y):
        moves = []
        piece_upper = piece.upper()

        if piece_upper == 'P':
            self.get_pawn_moves(piece, x, y, moves)
        elif piece_upper == 'R':
            self.get_rook_moves(x, y, moves)
        elif piece_upper == 'N':
            self.get_knight_moves(x, y, moves)
        elif piece_upper == 'B':
            self.get_bishop_moves(x, y, moves)
        elif piece_upper == 'K':
            self.get_king_moves(x, y, moves)
        elif piece_upper == 'Q':
            self.get_queen_moves(x, y, moves)

        return moves

    def verify_moviment(self, piece, x, y):
        next_piece = self.board[y][x]

        if next_piece == EMPTY_STATE or next_piece.isupper() != piece.isupper():
            return True

        return False

    def get_pawn_moves(self, piece, x, y, moves):
        if piece.isupper():
            if y < 7 and self.board[y + 1][x] == EMPTY_STATE:
                moves.append([y + 1, x])
            if y == 1 and self.board[y + 2][x] == EMPTY_STATE:
                moves.append([y + 2, x])
            if x < 7 and y < 7 and self.board[y + 1][x + 1] != EMPTY_STATE and self.board[y + 1][x + 1].islower():
                moves.append([y + 1, x + 1])
            if x > 0 and y < 7 and self.board[y + 1][x - 1] != EMPTY_STATE and self.board[y + 1][x - 1].islower():
                moves.append([y + 1, x - 1])
        else:
            if y > 0 and self.board[y - 1][x] == EMPTY_STATE:
                moves.append([y - 1, x])
            if y == 6 and self.board[y - 2][x] == EMPTY_STATE:
                moves.append([y - 2, x])
            if x > 0 and y > 0 and self.board[y - 1][x - 1] != EMPTY_STATE and self.board[y - 1][x - 1].isupper():
                moves.append([y - 1, x - 1])
            if x < 7 and y > 0 and self.board[y - 1][x + 1] != EMPTY_STATE and self.board[y - 1][x + 1].isupper():
                moves.append([y - 1, x + 1])

    def get_rook_moves(self, x, y, moves):
        for i in range(8):
            if 0 <= y + i < 8 and 0 <= x < 8 and self.verify_piece_not_exists(x, y + i) \
                    and [y + i, x] not in moves:
                moves.append([y + i, x])
            if 0 <= y - i < 8 and 0 <= x < 8 and self.verify_piece_not_exists(x, y - i) \
                    and [y - i, x] not in moves:
                moves.append([y - i, x])
            if 0 <= y < 8 and 0 <= x + i < 8 and self.verify_piece_not_exists(x + i, y) \
                    and [y, x + i] not in moves:
                moves.append([y, x + i])
            if 0 <= y < 8 and 0 <= x - i < 8 and self.verify_piece_not_exists(x - i, y) \
                    and [y, x - i] not in moves:
                moves.append([y, x - i])

    @staticmethod
    def get_knight_moves(x, y, moves):
        moves.append([y + 1, x + 2])
        moves.append([y - 1, x + 2])
        moves.append([y + 2, x + 1])
        moves.append([y - 2, x + 1])
        moves.append([y - 1, x - 2])
        moves.append([y + 1, x - 2])
        moves.append([y + 2, x - 1])
        moves.append([y - 2, x - 1])

    def get_bishop_moves(self, x, y, moves):
        for i in range(8):
            if 0 <= y + i < 8 and 0 <= x + i < 8 and self.verify_piece_not_exists(x + i, y + i):
                moves.append([y + i, x + i])
            if 0 <= y - i < 8 and 0 <= x + i < 8 and self.verify_piece_not_exists(x + i, y - i):
                moves.append([y - i, x + i])
            if 0 <= y + i < 8 and 0 <= x - i < 8 and self.verify_piece_not_exists(x - i, y + i):
                moves.append([y + i, x - i])
            if 0 <= y - i < 8 and 0 <= x - i < 8 and self.verify_piece_not_exists(x - i, y - i):
                moves.append([y - i, x - i])

    def get_queen_moves(self, x, y, moves):
        self.get_rook_moves(x, y, moves)
        self.get_bishop_moves(x, y, moves)

    @staticmethod
    def get_king_moves(x, y, moves):
        moves.append([y + 1, x - 1])
        moves.append([y + 1, x])
        moves.append([y + 1, x + 1])
        moves.append([y, x - 1])
        moves.append([y, x + 1])
        moves.append([y - 1, x - 1])
        moves.append([y - 1, x])
        moves.append([y - 1, x + 1])
