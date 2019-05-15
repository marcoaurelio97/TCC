from movement_rules import Movement
import random


class Minimax:

    @staticmethod
    def get_minimax_move(chessboard):
        moves = Movement.get_all_moves(chessboard.board)

        return random.choice(moves)
