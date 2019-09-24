from Minimax.penalties import Penalties
from Chess.movement_rules import Movement
import numpy as np


EMPTY_STATE = '.'
BLACK = -1
WHITE = 1


class Evaluation:

    @staticmethod
    def evaluate(board, player_turn):
        score = 0

        score += Evaluation().material(board)
        score += Evaluation().square(board, player_turn)
        score += Evaluation().mobility(board, player_turn)

        return score

    @staticmethod
    def material(board):
        score = 0
        piece_values = {'p': 128, 'b': 830, 'n': 782, 'r': 1289, 'q': 2529, 'k': 0}

        for y in range(0, 8):
            for x in range(0, 8):
                piece = board[y][x]
                if piece is not EMPTY_STATE:
                    if piece.islower():
                        score += piece_values[piece]
                    elif piece.isupper():
                        score -= piece_values[piece.lower()]

        return score

    @staticmethod
    def square(board, player_turn):
        score = 0

        for y in range(0, 8):
            for x in range(0, 8):
                piece = board[y][x]
                if piece is not EMPTY_STATE:
                    if player_turn == BLACK and piece.islower():
                        score += Penalties.get_score_by_piece(piece, x, y)
                    elif player_turn == WHITE and piece.isupper():
                        score += Penalties.get_score_by_piece(piece, x, y)

        return score

    @staticmethod
    def mobility():
        return 0

    @staticmethod
    def generate_mobility_area(board, player_turn):
        mob_area_board = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ])

        for y in range(0, 8):
            for x in range(0, 8):
                if player_turn == BLACK and board[y][x] != 'p' and board[y][x] != 'P' and board[y][x] != 'q' and board[y][x] != 'k':
                    mob_area_board[y][x] = 1

                if player_turn == WHITE and board[y][x] != 'p' and board[y][x] != 'P' and board[y][x] != 'Q' and board[y][x] != 'Q':
                    mob_area_board[y][x] = 1

        return mob_area_board

    @staticmethod
    def knight_attack(board, player_turn):
        mobility_area = Evaluation().generate_mobility_area(board, player_turn)

        possible_moves = []

        knight_positions = board.where == 'k' if player_turn == BLACK else board.where == 'K'

        for i in range(0, len(knight_positions[0])):
            Movement().get_knight_moves(board, knight_positions[0][i], knight_positions[1][i], possible_moves)

        possible_attack = 0
        for next_y, next_x in possible_moves:
            if mobility_area[next_y][next_x] == 1:
                possible_attack += 1

        return possible_attack
