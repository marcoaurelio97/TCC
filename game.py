from Chess.chessboard import *
from Minimax.minimax import *
from Chess.player import *
import traceback
import numpy as np


class Game:
    def __init__(self, op):
        self.chessboard = Chessboard()
        self.black_score = 0
        self.white_score = 0
        self.op = op

    def run(self):
        self.chessboard.print_board()
        while True:
            try:
                if not self.game_over():
                    if self.op == '1':
                        y_curr, x_curr, y_next, x_next = Minimax(3).get_minimax_move(self.chessboard, 1)
                    else:
                        y_curr, x_curr, y_next, x_next = get_player_move()

                    self.chessboard.move(x_curr, y_curr, x_next, y_next)
                    self.chessboard.print_board()

                if not self.game_over():
                    y_curr, x_curr, y_next, x_next = Minimax(3).get_minimax_move(self.chessboard, -1)
                    self.chessboard.move(x_curr, y_curr, x_next, y_next)
                    self.chessboard.print_board()

            except Exception as ex:
                input(traceback.format_exc())
            if self.game_over():
                break

    def game_over(self):
        unique, counts = np.unique(self.chessboard.board, return_counts=True)
        dict_counts = dict(zip(unique, counts))
        #print(dict_counts)
        if dict_counts['k'] == 0 or dict_counts['K'] == 0:
            return True
        return False

