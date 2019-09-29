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
        self.last_moves = []

    def run(self):
        game_time = time()
        self.chessboard.print_board(self.play)
        while True:
            try:
                if not self.game_over():
                    t = time()
                    if self.op == '1':
                        y_curr, x_curr, y_next, x_next, eval_states = \
                            Minimax(3).get_minimax_move(self.chessboard, 1, self.last_moves)
                    else:
                        y_curr, x_curr, y_next, x_next = get_player_move()

                    self.time_of_plays.append(round(time() - t, 3))
                    self.evaluated_moves.append(eval_states)

                    self.chessboard.move(x_curr, y_curr, x_next, y_next)
                    self.last_moves.append([y_curr, x_curr, y_next, x_next])
                    if len(self.last_moves) > 6:
                        self.last_moves.pop(0)
                    self.play += 1
                    self.chessboard.print_board(self.play)
                else:
                    print(f"Game Over - Vencedor - Preto")
                    print(f"Número de Jogadas: {self.play}")
                    print(f"Tempo de Jogo: {round(time() - game_time, 3)}s")
                    input()
                    break

                if not self.game_over():
                    t = time()
                    y_curr, x_curr, y_next, x_next, eval_states = \
                        Minimax(3).get_minimax_move(self.chessboard, -1, self.last_moves)

                    self.time_of_plays.append(round(time() - t, 3))
                    self.evaluated_moves.append(eval_states)

                    self.chessboard.move(x_curr, y_curr, x_next, y_next)
                    self.last_moves.append([y_curr, x_curr, y_next, x_next])
                    if len(self.last_moves) > 6:
                        self.last_moves.pop(0)
                    self.play += 1
                    self.chessboard.print_board(self.play)
                else:
                    print(f"Game Over - Vencedor - Branco")
                    print(f"Número de Jogadas: {self.play}")
                    print(f"Tempo de Jogo: {round(time() - game_time, 3)}s")
                    input()
                    break

            except Exception as ex:
                input(traceback.format_exc())

    def game_over(self):
        black_king = np.count_nonzero(self.chessboard.board == 'k')
        white_king = np.count_nonzero(self.chessboard.board == 'K')

        if not white_king or not black_king:
            return True
        return False

