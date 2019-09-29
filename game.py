from Chess.chessboard import *
from Minimax.minimax import *
from Chess.player import *
import traceback
import numpy as np
from time import time


class Game:
    def __init__(self, op):
        self.chessboard = Chessboard()
        self.black_score = 0
        self.white_score = 0
        self.op = op
        self.play = 0
        self.time_of_plays = []
        self.evaluated_moves = []

    def run(self):
        self.chessboard.print_board(self.play)
        while True:
            try:
                if not self.game_over():
                    t = time()
                    if self.op == '1':
                        y_curr, x_curr, y_next, x_next, eval_states = Minimax(3).get_minimax_move(self.chessboard, 1)
                    else:
                        y_curr, x_curr, y_next, x_next = get_player_move()
                    self.time_of_plays.append(round(time() - t, 3))
                    self.evaluated_moves.append(eval_states)

                    self.chessboard.move(x_curr, y_curr, x_next, y_next)
                    self.play += 1
                    self.chessboard.print_board(self.play)

                if not self.game_over():
                    t = time()
                    y_curr, x_curr, y_next, x_next, eval_states = Minimax(3).get_minimax_move(self.chessboard, -1)
                    self.time_of_plays.append(round(time() - t, 3))
                    self.evaluated_moves.append(eval_states)

                    self.chessboard.move(x_curr, y_curr, x_next, y_next)
                    self.play += 1
                    self.chessboard.print_board(self.play)

            except Exception as ex:
                input(traceback.format_exc())
            if self.game_over():
                break

    def game_over(self):
        black_king = np.count_nonzero(self.chessboard.board == 'k')
        white_king = np.count_nonzero(self.chessboard.board == 'K')

        if not white_king or not black_king:
            return True
        return False

