from Chess.movement_rules import Movement
from Minimax.evaluation import Evaluation
from copy import deepcopy

EMPTY_STATE = '.'
BLACK = -1 #black
WHITE = 1 #white


class State:

    def __init__(self, board, initial_y=None, initial_x=None, final_y=None, final_x=None, player=None):
        self.player_turn = player
        self.initial_y, self.initial_x, self.final_y, self.final_x = initial_y, initial_x, final_y, final_x
        self.board = board
        self.children = []

    def generate_children(self, player):
        for y in range(0, 8):
            for x in range(0, 8):
                if self.board[y][x] != EMPTY_STATE:
                    if player == BLACK and self.board[y][x].islower():
                        iteration_moves = Movement.get_moves(self.board, self.board[y][x], x, y)
                        for next_y, next_x in iteration_moves:
                            new_board = deepcopy(self.board)

                            # swap
                            piece = new_board[y][x]
                            new_board[y][x] = EMPTY_STATE
                            new_board[next_y][next_x] = piece

                            self.children.append(
                                State(new_board, y, Movement.letters[x], next_y, Movement.letters[next_x], player))

                    elif player == WHITE and self.board[y][x].isupper():
                        iteration_moves = Movement.get_moves(self.board, self.board[y][x], x, y)
                        for next_y, next_x in iteration_moves:
                            new_board = deepcopy(self.board)

                            # swap
                            piece = new_board[y][x]
                            new_board[y][x] = EMPTY_STATE
                            new_board[next_y][next_x] = piece

                            self.children.append(
                                State(new_board, y, Movement.letters[x], next_y, Movement.letters[next_x], player))

    def get_score(self, initial_player):
        if initial_player == BLACK:
            return Evaluation().evaluate_black(self.board)
        else:
            return Evaluation().evaluate_white(self.board)
