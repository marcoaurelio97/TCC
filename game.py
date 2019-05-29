from chessboard import *
from functions import *
from minimax import *


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
                        y_curr, x_curr, y_next, x_next = Minimax().get_minimax_move(self.chessboard, 1)
                    else:
                        y_curr, x_curr, y_next, x_next = get_player_move()

                    self.chessboard.move(x_curr, y_curr, x_next, y_next)
                    self.chessboard.print_board()

                if not self.game_over():
                    y_curr, x_curr, y_next, x_next = Minimax().get_minimax_move(self.chessboard, -1)
                    self.chessboard.move(x_curr, y_curr, x_next, y_next)
                    self.chessboard.print_board()

            except Exception as ex:
                input("{} - Press any key to continue...".format(ex))
            if self.game_over():
                break

    def game_over(self):
        count = 0
        for y in range(0, 8):
            for x in range(0, 8):
                if self.chessboard.board[y][x] == 'K' or self.chessboard.board[y][x] == 'k':
                    count += 1

        if count == 1:
            return True
        return False

