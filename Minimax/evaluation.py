from Minimax.penalties import PsqtBonus
from Chess.movement_rules import Movement
import numpy as np


EMPTY_STATE = '.'
BLACK = -1
WHITE = 1


class Evaluation:
    mobility_bonus = np.array([
        [-62, -53, -12, -4, 3, 13, 22, 28, 33],
        [-48, -20, 16, 26, 38, 51, 55, 63, 63, 68, 81, 81, 91, 98],
        [-58, -27, -15, -10, -5, -2, 9, 16, 30, 29, 32, 38, 46, 48, 58],
        [-39, -21, 3, 3, 14, 22, 28, 41, 43, 48, 56, 60, 60, 66, 67, 70, 71, 73, 79, 88, 88, 99, 102, 102, 106, 109, 113, 116]
    ])

    king_attackers_weight = np.array([77, 55, 44, 10])

    @staticmethod
    def evaluate(board):
        score = 0

        score += Evaluation().material(board)
        score += Evaluation().square(board)
        score += Evaluation().mobility(board, WHITE) - Evaluation().mobility(board, BLACK)
        score += Evaluation().king_safety(board, WHITE) - Evaluation().king_safety(board, BLACK)

        return score

    @staticmethod
    def material(board):
        score = 0
        piece_values = {'p': 128, 'b': 830, 'n': 782, 'r': 1289, 'q': 2529, 'k': 10000}

        for y in range(0, 8):
            for x in range(0, 8):
                piece = board[y][x]
                if piece is not EMPTY_STATE:
                    if piece.islower():
                        score -= piece_values[piece]
                    elif piece.isupper():
                        score += piece_values[piece.lower()]
        return score

    @staticmethod
    def square(board):
        score = 0

        for y in range(0, 8):
            for x in range(0, 8):
                piece = board[y][x]
                if piece is not EMPTY_STATE:
                    if piece.islower():
                        score -= PsqtBonus().get_score_by_piece(piece, x, y)
                    elif piece.isupper():
                        score += PsqtBonus().get_score_by_piece(piece, x, y)

        return score

    @staticmethod
    def mobility(board, player_turn):
        score = 0

        mobility_area = Evaluation().generate_mobility_area(board, player_turn)

        i, _ = Evaluation().knight_attack(board, player_turn, mobility_area)
        if i < len(Evaluation().mobility_bonus[0]):
            score += Evaluation().mobility_bonus[0][i]

        i, _ = Evaluation().bishop_attack(board, player_turn, mobility_area)
        if i < len(Evaluation().mobility_bonus[1]):
            score += Evaluation().mobility_bonus[1][i]

        i, _ = Evaluation().rook_attack(board, player_turn, mobility_area)
        if i < len(Evaluation().mobility_bonus[2]):
            score += Evaluation().mobility_bonus[2][i]

        i, _ = Evaluation().queen_attack(board, player_turn, mobility_area)
        if i < len(Evaluation().mobility_bonus[3]):
            score += Evaluation().mobility_bonus[3][i]

        return score

    @staticmethod
    def generate_mobility_area(board, player_turn):
        mob_area_board = np.array([
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ])

        for y in range(0, 8):
            for x in range(0, 8):
                if player_turn == BLACK:
                    if board[y][x] == 'q' or board[y][x] == 'k':
                        mob_area_board[y][x] = 0
                    if (y < 7 and x > 0 and board[y - 1][x - 1] == 'P') or (y < 7 and x < 7 and board[y - 1][x + 1] == 'P'):
                        mob_area_board[y][x] = 0
                    if board[y][x] == 'p' and (y > 4 or board[y-1][x] != EMPTY_STATE):
                        mob_area_board[y][x] = 0

                if player_turn == WHITE:
                    if board[y][x] == 'Q' or board[y][x] == 'K':
                        mob_area_board[y][x] = 0
                    if (y < 7 and x > 0 and board[y + 1][x - 1] == 'p') or (y < 7 and x < 7 and board[y + 1][x + 1] == 'p'):
                        mob_area_board[y][x] = 0
                    if board[y][x] == 'P' and (y < 3 or board[y+1][x] != EMPTY_STATE):
                        mob_area_board[y][x] = 0

        return mob_area_board

    @staticmethod
    def knight_attack(board, player_turn, comparison_board):
        possible_moves = {}

        knight_positions = np.where(board == 'n' if player_turn == BLACK else board == 'N')

        for i in range(0, len(knight_positions[0])):
            i_moves = []
            Movement().get_knight_moves(board, knight_positions[1][i], knight_positions[0][i], i_moves)
            possible_moves[f"{knight_positions[0][i]}{knight_positions[1][i]}"] = i_moves

        possible_attack = 0
        number_of_attackers = 0

        for key in possible_moves:
            piece_attacked = False
            for value in possible_moves[key]:
                if comparison_board[value[0]][value[1]] == 1:
                    possible_attack += 1
                    if not piece_attacked:
                        number_of_attackers += 1
                        piece_attacked = True

        return possible_attack, number_of_attackers

    @staticmethod
    def rook_attack(board, player_turn, comparison_board):
        possible_moves = {}

        rook_positions = np.where(board == 'r' if player_turn == BLACK else board == 'R')

        for i in range(0, len(rook_positions[0])):
            i_moves = []
            Movement().get_knight_moves(board, rook_positions[1][i], rook_positions[0][i], i_moves)
            possible_moves[f"{rook_positions[1][i]}{rook_positions[0][i]}"] = i_moves

        possible_attack = 0
        number_of_attackers = 0

        for key in possible_moves:
            piece_attacked = False
            for value in possible_moves[key]:
                if comparison_board[value[0]][value[1]] == 1:
                    possible_attack += 1
                    if not piece_attacked:
                        number_of_attackers += 1
                        piece_attacked = True

        return possible_attack, number_of_attackers

    @staticmethod
    def queen_attack(board, player_turn, comparison_board):
        possible_moves = {}

        queen_positions = np.where(board == 'q' if player_turn == BLACK else board == 'Q')

        for i in range(0, len(queen_positions[0])):
            i_moves = []
            Movement().get_knight_moves(board, queen_positions[1][i], queen_positions[0][i], i_moves)
            possible_moves[f"{queen_positions[1][i]}{queen_positions[0][i]}"] = i_moves

        possible_attack = 0
        number_of_attackers = 0

        for key in possible_moves:
            piece_attacked = False
            for value in possible_moves[key]:
                if comparison_board[value[0]][value[1]] == 1:
                    possible_attack += 1
                    if not piece_attacked:
                        number_of_attackers += 1
                        piece_attacked = True

        return possible_attack, number_of_attackers

    @staticmethod
    def bishop_attack(board, player_turn, comparison_board):
        possible_moves = {}

        bishop_positions = np.where(board == 'b' if player_turn == BLACK else board == 'B')

        for i in range(0, len(bishop_positions[0])):
            i_moves = []
            Movement().get_knight_moves(board, bishop_positions[1][i], bishop_positions[0][i], i_moves)
            possible_moves[f"{bishop_positions[1][i]}{bishop_positions[0][i]}"] = i_moves

        possible_attack = 0
        number_of_attackers = 0

        for key in possible_moves:
            piece_attacked = False
            for value in possible_moves[key]:
                if comparison_board[value[0]][value[1]] == 1:
                    possible_attack += 1
                    if not piece_attacked:
                        number_of_attackers += 1
                        piece_attacked = True

        return possible_attack, number_of_attackers

    @staticmethod
    def king_safety(board, player_turn):
        weight, king_attackers = Evaluation().king_attackers(board, player_turn)

        no_queen = np.count_nonzero(board == 'q' if player_turn == BLACK else board == 'Q')

        score = 0
        score -= weight
        score -= 69 * king_attackers
        score -= 873 * no_queen

        return score

    @staticmethod
    def king_attackers(board, player_turn):
        king_ring = Evaluation().generate_king_ring(board, player_turn)

        weight = 0
        king_attacks = 0

        qty_attacks, qty_attackers = Evaluation().knight_attack(board, -player_turn, king_ring)
        weight += Evaluation().king_attackers_weight[0] * qty_attackers
        king_attacks += qty_attacks

        qty_attacks, qty_attackers = Evaluation().bishop_attack(board, -player_turn, king_ring)
        weight += Evaluation().king_attackers_weight[1] * qty_attackers
        king_attacks += qty_attacks

        qty_attacks, qty_attackers = Evaluation().rook_attack(board, -player_turn, king_ring)
        weight += Evaluation().king_attackers_weight[2] * qty_attackers
        king_attacks += qty_attacks

        qty_attacks, qty_attackers = Evaluation().queen_attack(board, -player_turn, king_ring)
        weight += Evaluation().king_attackers_weight[3] * qty_attackers
        king_attacks += qty_attacks

        return weight, king_attacks

    @staticmethod
    def generate_king_ring(board, player_turn):
        king_ring_board = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ])

        king = 'k' if player_turn == BLACK else 'K'
        king_positions = np.where(board == king)

        if len(king_positions[0]) == 0:
            return king_ring_board

        king_y = king_positions[0][0]
        king_x = king_positions[1][0]

        for iy in range(-1, 2):
            for ix in range(-1, 2):
                index_y = king_y + iy
                index_x = king_x + ix

                if player_turn == WHITE:
                    if 0 <= index_y <= 7 and 0 <= index_x <= 7:
                        king_ring_board[index_y][index_x] = 1

                        if index_y > 0 and 0 < index_x < 7:
                            if board[index_y - 1][index_x - 1] == 'P' and board[index_y - 1][index_x + 1] == 'P':
                                king_ring_board[index_y][index_x] = 0

                if player_turn == BLACK:
                    if 0 <= index_y <= 7 and 0 <= index_x <= 7:
                        king_ring_board[index_y][index_x] = 1

                        if index_y < 7 and 0 < index_x < 7:
                            if board[index_y + 1][index_x - 1] == 'p' and board[index_y + 1][index_x + 1] == 'p':
                                king_ring_board[index_y][index_x] = 0

        return king_ring_board

