from Minimax.penalties import Penalties
from Chess.movement_rules import Movement
import numpy as np

EMPTY_STATE = '.'
BLACK = -1
WHITE = 1


class Evaluation:
    end_game = False
    mid_game = False

    mobility_bonus_mg = np.array([
        [-62, -53, -12, -4, 3, 13, 22, 28, 33],
        [-48, -20, 16, 26, 38, 51, 55, 63, 63, 68, 81, 81, 91, 98],
        [-58, -27, -15, -10, -5, -2, 9, 16, 30, 29, 32, 38, 46, 48, 58],
        [-39, -21, 3, 3, 14, 22, 28, 41, 43, 48, 56, 60, 60, 66, 67, 70, 71, 73, 79, 88, 88, 99, 102, 102, 106, 109, 113, 116]
    ])

    mobility_bonus_eg = np.array([
        [-81, -56, -30, -14, 8, 15, 23, 27, 33],
        [-59, -23, -3, 13, 24, 42, 54, 57, 65, 73, 78, 86, 88, 97],
        [-76, -18, 28, 55, 69, 82, 112, 118, 132, 142, 155, 165, 166, 169, 171],
        [-36, -15, 8, 18, 34, 54, 61, 73, 79, 92, 94, 104, 113, 120, 123, 126, 133, 136, 140, 143, 148, 166, 170, 175, 184, 191, 206, 212]
    ])

    @staticmethod
    def evaluate(board):
        score = 0

        score += Evaluation().material(board)
        score += Evaluation().square(board)
        score += Evaluation().mobility(board, WHITE) - Evaluation().mobility(board, BLACK)
        score += Evaluation().pawns_structure(board, WHITE) - Evaluation().pawns_structure(board, BLACK)

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
                        score -= Penalties.get_score_by_piece(piece, x, y)
                    elif piece.isupper():
                        score += Penalties.get_score_by_piece(piece, x, y)

        return score

    @staticmethod
    def mobility(board, player_turn):
        score = 0

        i = Evaluation().knight_attack(board, player_turn)
        if i < len(Evaluation().mobility_bonus_mg[0]):
            score += Evaluation().mobility_bonus_mg[0][i]

        i = Evaluation().bishop_attack(board, player_turn)
        if i < len(Evaluation().mobility_bonus_mg[1]):
            score += Evaluation().mobility_bonus_mg[1][i]

        i = Evaluation().rook_attack(board, player_turn)
        if i < len(Evaluation().mobility_bonus_mg[2]):
            score += Evaluation().mobility_bonus_mg[2][i]

        i = Evaluation().queen_attack(board, player_turn)
        if i < len(Evaluation().mobility_bonus_mg[3]):
            score += Evaluation().mobility_bonus_mg[3][i]

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
                    if board[y][x] == "q" or board[y][x] == "k":
                        mob_area_board[y][x] = 0
                    if (y < 7 and x > 0 and board[y - 1][x - 1] == "P") or (y < 7 and x < 7 and board[y - 1][x + 1] == "P"):
                        mob_area_board[y][x] = 0
                    if board[y][x] == "p" and (y > 4 or board[y-1][x] != EMPTY_STATE):
                        mob_area_board[y][x] = 0

                if player_turn == WHITE:
                    if board[y][x] == "Q" or board[y][x] == "K":
                        mob_area_board[y][x] = 0
                    if (y < 7 and x > 0 and board[y + 1][x - 1] == "p") or (y < 7 and x < 7 and board[y + 1][x + 1] == "p"):
                        mob_area_board[y][x] = 0
                    if board[y][x] == "P" and (y < 3 or board[y+1][x] != EMPTY_STATE):
                        mob_area_board[y][x] = 0

        return mob_area_board

    @staticmethod
    def knight_attack(board, player_turn):
        mobility_area = Evaluation().generate_mobility_area(board, player_turn)

        possible_moves = []

        knight_positions = np.where(board == 'n' if player_turn == BLACK else board == 'N')

        for i in range(0, len(knight_positions[0])):
            Movement().get_knight_moves(board, knight_positions[1][i], knight_positions[0][i], possible_moves)

        possible_attack = 0

        for next_y, next_x in possible_moves:
            if mobility_area[next_y][next_x] == 1:
                possible_attack += 1
        return possible_attack

    @staticmethod
    def rook_attack(board, player_turn):
        mobility_area = Evaluation().generate_mobility_area(board, player_turn)

        possible_moves = []

        rook_positions = np.where(board == 'r' if player_turn == BLACK else board == 'R')

        for i in range(0, len(rook_positions[0])):
            Movement().get_rook_moves(board, rook_positions[1][i], rook_positions[0][i], possible_moves, True)

        possible_attack = 0
        for next_y, next_x in possible_moves:
            if mobility_area[next_y][next_x] == 1:
                possible_attack += 1

        return possible_attack

    @staticmethod
    def queen_attack(board, player_turn):
        mobility_area = Evaluation().generate_mobility_area(board, player_turn)

        possible_moves = []

        queen_positions = np.where(board == 'q' if player_turn == BLACK else board == 'Q')

        for i in range(0, len(queen_positions[0])):
            Movement().get_queen_moves(board, queen_positions[1][i], queen_positions[0][i], possible_moves, True)

        possible_attack = 0

        for next_y, next_x in possible_moves:
            if mobility_area[next_y][next_x] == 1:
                possible_attack += 1

        return possible_attack

    @staticmethod
    def bishop_attack(board, player_turn):
        mobility_area = Evaluation().generate_mobility_area(board, player_turn)

        possible_moves = []

        bishop_positions = np.where(board == 'b' if player_turn == BLACK else board == 'B')

        for i in range(0, len(bishop_positions[0])):
            Movement().get_bishop_moves(board, bishop_positions[1][i], bishop_positions[0][i], possible_moves, True)

        possible_attack = 0
        for next_y, next_x in possible_moves:
            if mobility_area[next_y][next_x] == 1:
                possible_attack += 1

        return possible_attack

    @staticmethod
    def pawns_structure(board, player_turn):
        score = 0

        score -= Evaluation().isolated_pawn(board, player_turn)
        score -= Evaluation().doubled_pawn(board, player_turn)
        score -= Evaluation().backward_pawn(board, player_turn)
        # score += Evaluation().connected_pawn_bonus(board, player_turn)

        return score

    @staticmethod
    def isolated_pawn(board, player_turn):
        isolated_score = 0
        pawn_positions = np.where(board == "p" if player_turn == BLACK else board == "P")
        pawn = "p" if player_turn == BLACK else "P"

        for i in range(0, len(pawn_positions[0])):
            isolated = False
            y_pawn, x_pawn = pawn_positions[0][i], pawn_positions[1][i]

            for y in range(0, 8):
                if x_pawn == 0:
                    if board[y][x_pawn + 1] == pawn:
                        isolated = False
                        break
                elif x_pawn == 7:
                    if board[y][x_pawn - 1] == pawn:
                        isolated = False
                        break
                elif board[y][x_pawn + 1] == pawn or board[y][x_pawn - 1] == pawn:
                    isolated = False
                    break
                else:
                    isolated = True

            if isolated:
                isolated_score += 5

        return isolated_score

    @staticmethod
    def doubled_pawn(board, player_turn):
        doubled_score = 0
        pawn_positions = np.where(board == "p" if player_turn == BLACK else board == "P")

        for i in range(0, len(pawn_positions[0])):
            y_pawn, x_pawn = pawn_positions[0][i], pawn_positions[1][i]

            if player_turn == WHITE:
                if y_pawn < 7 and board[y_pawn + 1][x_pawn] != "P":
                    continue
                elif x_pawn > 0 and board[y_pawn][x_pawn - 1] == "P":
                    continue
                elif x_pawn < 7 and board[y_pawn][x_pawn + 1] == "P":
                    continue
                else:
                    doubled_score += 11
            elif player_turn == BLACK:
                if y_pawn > 0 and board[y_pawn - 1][x_pawn] != "p":
                    continue
                elif x_pawn > 0 and board[y_pawn][x_pawn - 1] == "p":
                    continue
                elif x_pawn < 7 and board[y_pawn][x_pawn + 1] == "p":
                    continue
                else:
                    doubled_score += 11

        return doubled_score

    @staticmethod
    def backward_pawn(board, player_turn):
        backward_score = 0
        pawn_positions = np.where(board == "p" if player_turn == BLACK else board == "P")

        for i in range(0, len(pawn_positions[0])):
            backward = False
            y_pawn, x_pawn = pawn_positions[0][i], pawn_positions[1][i]

            if player_turn == WHITE:
                for y in range(0, y_pawn + 1):
                    if (x_pawn > 0 and board[y][x_pawn - 1] == "P")\
                            or (x_pawn < 7 and board[y][x_pawn + 1] == "P"):
                        backward = True
                        break
                if backward or Evaluation().isolated_pawn(board, player_turn):
                    continue
                if y_pawn < 6:
                    if (x_pawn > 0 and board[y_pawn + 2][x_pawn - 1] == "p")\
                            or (x_pawn < 7 and board[y_pawn + 2][x_pawn + 1] == "p"):
                        backward = True
                elif y_pawn < 7:
                    if board[y_pawn + 1][x_pawn] == "p":
                        backward = True

            if player_turn == BLACK:
                for y in range(y_pawn, 8):
                    if (x_pawn > 0 and board[y][x_pawn - 1] == "p")\
                            or (x_pawn < 7 and board[y][x_pawn + 1] == "p"):
                        backward = True
                        break
                if backward or Evaluation().isolated_pawn(board, player_turn):
                    continue
                if y_pawn > 1:
                    if (x_pawn > 0 and board[y_pawn - 2][x_pawn - 1] == "P")\
                            or (x_pawn < 7 and board[y_pawn - 2][x_pawn + 1] == "P"):
                        backward = True
                elif y_pawn > 0:
                    if board[y_pawn - 1][x_pawn] == "P":
                        backward = True

            if backward:
                backward_score += 9

        return backward_score

    @staticmethod
    def connected_pawn_bonus(board, player_turn):
        connected_score = 0
        pawn_positions = np.where(board == "p" if player_turn == BLACK else board == "P")
        seed = [0, 7, 8, 12, 29, 48, 86]

        for i in range(0, len(pawn_positions[0])):
            y_pawn, x_pawn = pawn_positions[0][i], pawn_positions[1][i]

            if not Evaluation().connected_pawn(board, player_turn, y_pawn, x_pawn):
                break

            op = Evaluation().opposed_pawn(board, player_turn, y_pawn, x_pawn)
            ph = Evaluation().phalanx_pawn(board, player_turn, y_pawn, x_pawn)
            su = Evaluation().supported_pawn(board, player_turn, y_pawn, x_pawn)
            r = 7 - y_pawn

            if r < 2 or r > 7:
                break

            connected_score += (int(seed[r - 1] * (3 if ph else 2) / (2 if op else 1)) >> 0) + 17 * su

        return connected_score

    @staticmethod
    def connected_pawn(board, player_turn, y_pawn, x_pawn):
        if Evaluation().supported_pawn(board, player_turn, y_pawn, x_pawn)\
                or Evaluation().phalanx_pawn(board, player_turn, y_pawn, x_pawn):
            return True

        return False

    @staticmethod
    def supported_pawn(board, player_turn, y_pawn, x_pawn):
        supported_score = 0
        if player_turn == WHITE:
            if y_pawn < 7:
                if x_pawn > 0 and board[y_pawn + 1][x_pawn - 1] == "P":
                    supported_score += 1
                if x_pawn < 7 and board[y_pawn + 1][x_pawn + 1] == "P":
                    supported_score += 1
        elif player_turn == BLACK:
            if y_pawn > 0:
                if x_pawn > 0 and board[y_pawn - 1][x_pawn - 1] == "p":
                    supported_score += 1
                if x_pawn < 7 and board[y_pawn - 1][x_pawn + 1] == "p":
                    supported_score += 1

        return supported_score

    @staticmethod
    def phalanx_pawn(board, player_turn, y_pawn, x_pawn):
        pawn = "p" if player_turn == BLACK else "P"

        if (x_pawn > 0 and board[y_pawn][x_pawn - 1] == pawn)\
                or (x_pawn < 7 and board[y_pawn][x_pawn + 1] == pawn):
            return 1

        return 0

    @staticmethod
    def opposed_pawn(board, player_turn, y_pawn, x_pawn):
        if player_turn == WHITE:
            for y in range(7, y_pawn, -1):
                if board[y][x_pawn] == "p":
                    return 1
        elif player_turn == BLACK:
            for y in range(0, y_pawn):
                if board[y][x_pawn] == "P":
                    return 1

        return 0
