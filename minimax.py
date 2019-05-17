from state import State
from sys import maxsize as inf

EMPTY_STATE = '.'

AI = -1
HUMAN = 1


class Minimax:

    @staticmethod
    def get_minimax_move(chessboard):
        initial_state = State(chessboard.board)
        move_score = Minimax.search(initial_state, 3, AI)

        # print("Best Score:\t{}".format(move_score))

        initial_state.generate_children()

        # Correct error
        # local variable 'best_state' referenced before assignment

        for move in initial_state.children:
            if move.score <= move_score:
                best_state = move

        next_move = best_state.initial_y, best_state.initial_x, best_state.final_y, best_state.final_x

        return next_move

    @staticmethod
    def search(state, depth, player):
        # print("--------------------- /{}/ -------------------".format(state.score))
        # state.print_state()

        if depth == 0:
            return state.score

        state.generate_children()

        if player == AI:
            return max([Minimax.search(child, depth-1, -player) for child in state.children])
        elif player == HUMAN:
            return min([Minimax.search(child, depth-1, -player) for child in state.children])
