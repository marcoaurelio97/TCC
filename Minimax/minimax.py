from Minimax.state import State
from database import Database
from math import inf as infinite

EMPTY_STATE = '.'
WHITE = -1
BLACK = 1
MINIMAX_DEPTH = 3


class Minimax:
    @staticmethod
    def get_minimax_move(chessboard, player):
        initial_state = State(chessboard.board)

        positions = Database().get("positions", chessboard.board)
        if positions:
            next_move = positions["y_curr"], positions["x_curr"], positions["y_next"], positions["x_next"]
        else:
            best_state = Minimax.search(initial_state, MINIMAX_DEPTH, player)
            next_move = best_state.initial_y, best_state.initial_x, best_state.final_y, best_state.final_x

            Database().insert("positions", chessboard.board, best_state.initial_y, best_state.initial_x,
                              best_state.final_y, best_state.final_x)

        return next_move

    @staticmethod
    def search(state, depth, player):
        if depth == 0:
            return state.score

        state.generate_children(player)

        if player == BLACK:
            if depth == 1:
                list_search = [Minimax.search(child, depth-1, -player) for child in state.children]
                if list_search:
                    state.score = max(list_search)
            elif depth == MINIMAX_DEPTH:
                return_state = State([])
                return_state.score = -infinite

                for child in state.children:
                    Database().insert("positions", child.board, child.initial_y, child.initial_x,
                                      child.final_y, child.final_x)
                    Minimax.search(child, depth - 1, -player)
                    return_state = child if child.score > return_state.score else return_state
                return return_state
            else:
                state.score = -infinite
                for child in state.children:
                    Minimax.search(child, depth - 1, -player)
                    state.score = child.score if child.score > state.score else state.score
                return state.score
        elif player == WHITE:
            if depth == 1:
                list_search = [Minimax.search(child, depth-1, -player) for child in state.children]
                if list_search:
                    state.score = min(list_search)
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
