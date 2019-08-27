from Minimax.state import State
from math import inf as infinite
# import time

EMPTY_STATE = '.'
WHITE = -1
BLACK = 1
MINIMAX_DEPTH = 4


class Minimax:
    @staticmethod
    def get_minimax_move(chessboard, player):
        initial_state = State(chessboard.board)

        # t = time()
        _, best_state = Minimax.search(initial_state, MINIMAX_DEPTH, player, -infinite, infinite)
        input("Time spent: {} seconds | Press enter to continue...")

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

        state.print_state()
        state.generate_children(player)
        best_value = -infinite if player == BLACK else infinite
        for child in state.children:
            eval_child, action_child = Minimax.search(child, depth-1, -player, alpha, beta)

            if player == BLACK and best_value < eval_child:
                best_value = eval_child
                action_target = child
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break

            elif player == WHITE and best_value > eval_child:
                best_value = eval_child
                action_target = child
                beta = min(beta, best_value)
                if beta <= alpha:
                    break

        return best_value, action_target


