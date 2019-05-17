from movement_rules import Movement
from copy import deepcopy

EMPTY_STATE = '.'


class State:
    initial_y, initial_x, final_y, final_x = None, None, None, None
    board, score = None, None
    children = None

    def __init__(self, board, initial_y=None, initial_x=None, final_y=None, final_x=None):
        self.initial_y, self.initial_x, self.final_y, self.final_x = initial_y, initial_x, final_y, final_x
        self.board = board
        self.children = []
        self.score = self.evaluate()

    def generate_children(self):
        for y in range(0, 8):
            for x in range(0, 8):
                if self.board[y][x] != EMPTY_STATE and self.board[y][x].islower():
                    iteration_moves = Movement.get_moves(self.board, self.board[y][x], x, y)
                    for k in iteration_moves:
                        new_board = deepcopy(self.board)

                        # swap
                        piece = new_board[y][x]
                        new_board[y][x] = EMPTY_STATE
                        new_board[k[0]][k[1]] = piece

                        self.children.append(State(new_board, y, Movement.letters[x], k[0], Movement.letters[k[1]]))

    def evaluate(self):
        score = 0
        score += self.material()

        return score

    def material(self):
        score = 0
        piece_values = {'p': 1, 'b': 3, 'n': 3, 'r': 5, 'q': 9, 'k': 0}

        for y in range(0, 8):
            for x in range(0, 8):
                piece = self.board[y][x]
                if piece is not EMPTY_STATE:
                    if piece.islower():
                        score += piece_values[piece]
                    elif piece.isupper():
                        score -= piece_values[piece.lower()]

        return score
