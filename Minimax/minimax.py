from Minimax.state import State
from math import inf as infinite

EMPTY_STATE = '.'

MINIMAZING_PLAYER = -1
MAXIMAZING_PLAYER = 1
MINIMAX_DEPTH = 2
evaluated_states = 0

class Minimax:

    def __init__(self, depth):
        self.depth = depth
        self.evaluated_states = 0

    def get_minimax_move(self, chessboard, player):
        initial_state = State(chessboard.board)

        best_state, _ = Minimax.search(initial_state, self.depth, player)

        if best_state:
            global evaluated_states
            next_move = best_state.initial_y, best_state.initial_x, best_state.final_y, best_state.final_x, evaluated_states

            return next_move
        else:
            for move in initial_state.children:
                print("Score: {}".format(move.score))
            raise Exception("Sorry but we could'n find the best move for this case!")

    @staticmethod
    def search(state, depth, player):
        global evaluated_states

        if depth == 0:
            return state, state.get_score()

        state.generate_children(player)

        if player == MINIMAZING_PLAYER:
            best_value = -infinite
            for child in state.children:
                eval_state, eval_score = Minimax.search(child, depth - 1, -player)

                evaluated_states += 1
                if eval_score > best_value:
                    best_state = child
                    best_value = eval_score

            return best_state, best_value
        elif player == MAXIMAZING_PLAYER:
            best_value = +infinite
            for child in state.children:
                eval_state, eval_score = Minimax.search(child, depth - 1, -player)

                evaluated_states += 1
                if eval_score < best_value:
                    best_state = child
                    best_value = eval_score

            return best_state, best_value
