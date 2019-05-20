from state import State
from math import inf as infinite
from time import time

EMPTY_STATE = '.'

AI = -1
HUMAN = 1
MINIMAX_DEPTH = 3

class Minimax:

    @staticmethod
    def get_minimax_move(chessboard):
        initial_state = State(chessboard.board)

        t = time()
        best_state = Minimax.search(initial_state, MINIMAX_DEPTH, AI)
        input("Time spent: {} segundos | Press enter to continue...".format(time() - t))

        if best_state:
            next_move = best_state.initial_y, best_state.initial_x, best_state.final_y, best_state.final_x

            return next_move
        else:
            for move in initial_state.children:
                print("Score: {}".format(move.score))
            raise Exception("Sorry but we could'n find the best move for this case!")

    @staticmethod
    def search(state, depth, player):

        if depth == 0:
            return state.score

        state.generate_children()

        if player == AI:
            if depth == 1:
                state.score = max([Minimax.search(child, depth-1, -player) for child in state.children])
            elif depth == MINIMAX_DEPTH:
                return_state = State([])
                return_state.score = -infinite

                for child in state.children:
                    Minimax.search(child, depth - 1, -player)
                    return_state = child if child.score > return_state.score else return_state
                return return_state
            else:
                state.score = -infinite
                for child in state.children:
                    Minimax.search(child, depth - 1, -player)
                    state.score = child.score if child.score > state.score else state.score
                return state.score
        elif player == HUMAN:
            if depth == 1:
                state.score = min([Minimax.search(child, depth-1, -player) for child in state.children])
            elif depth == MINIMAX_DEPTH:
                return_state = State([])
                return_state.score = +infinite

                for child in state.children:
                    Minimax.search(child, depth - 1, -player)
                    return_state = child if child.score < return_state.score else return_state
                return return_state
            else:
                state.score = +infinite
                for child in state.children:
                    Minimax.search(child, depth - 1, -player)
                    state.score = child.score if child.score < state.score else state.score
                return state.score



