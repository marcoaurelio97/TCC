from chessboard import *
from functions import *
from minimax import *


class Game:
    chessboard = None
    black_score = None
    white_score = None
    sum_time = 0
    number_of_moves = 0

    def __init__(self):
        self.chessboard = Chessboard()
        self.black_score = 0
        self.white_score = 0

    def run(self):
        while True:
            try:
                if not self.game_over():
                    # Player's Turn
                    # self.chessboard.print_board()
                    # y_curr, x_curr, y_next, x_next = get_player_move()
                    # self.chessboard.move(x_curr, y_curr, x_next, y_next)

                    # Teste AI vs AI
                    t = time()

                    y_curr, x_curr, y_next, x_next = Minimax().get_minimax_move(self.chessboard, -1)
                    self.chessboard.move(x_curr, y_curr, x_next, y_next)
                    self.chessboard.print_board()

                    self.number_of_moves += 1
                    self.sum_time += (time() - t)

                # AI's Turn
                if not self.game_over():
                    t = time()

                    y_curr, x_curr, y_next, x_next = Minimax().get_minimax_move(self.chessboard, 1)
                    self.chessboard.move(x_curr, y_curr, x_next, y_next)
                    self.chessboard.print_board()

                    self.number_of_moves += 1
                    self.sum_time += (time() - t)

            except Exception as ex:
                input("{} - Press any key to continue...".format(ex))
            if self.game_over():
                break

        print("Average time: {}".format(self.sum_time/self.number_of_moves))

    def game_over(self):
        count = 0
        for y in range(0, 8):
            for x in range(0, 8):
                if self.chessboard.board[y][x] == 'K' or self.chessboard.board[y][x] == 'k':
                    count += 1

        if count == 1:
            return True
        return False

