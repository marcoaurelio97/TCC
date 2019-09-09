from Minimax.state import State
from math import inf as infinite
from time import time

EMPTY_STATE = '.'

MINIMAZING_PLAYER = -1
MAXIMAZING_PLAYER = 1
MINIMAX_DEPTH = 4

class Minimax:

    def __init__(self, depth):
        self.depth = depth

    def get_minimax_move(self, chessboard, player):
        initial_state = State(chessboard.board)

        t = time()
        _, best_state = Minimax.search(initial_state, self.depth, player, -infinite, infinite)
        input("Time spent: {} seconds | Press enter to continue...".format(time()-t))

        if best_state:
            next_move = best_state.initial_y, best_state.initial_x, best_state.final_y, best_state.final_x

            return next_move
        else:
            for move in initial_state.children:
                print("Score: {}".format(move.score))
            raise Exception("Sorry but we could'n find the best move for this case!")

    @staticmethod
    def search(state, depth, player, alpha, beta):
        if depth == 0:
            return state.score, ""

        state.generate_children(player)
        best_value = -infinite if player == MAXIMAZING_PLAYER else infinite

        for child in state.children:
            eval_child, action_child = Minimax.search(child, depth-1, -player, alpha, beta)

            if player == MAXIMAZING_PLAYER and best_value < eval_child:
                best_value = eval_child
                action_target = child
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break

            elif player == MINIMAZING_PLAYER and best_value > eval_child:
                best_value = eval_child
                action_target = child
                beta = min(beta, best_value)
                if beta <= alpha:
                    break

        return best_value, action_target


