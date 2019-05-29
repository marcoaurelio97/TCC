from movement_rules import Movement
from copy import deepcopy

EMPTY_STATE = '.'
AI = -1
HUMAN = 1


class State:
    initial_y = initial_x = final_y = final_x = None
    board = None
    children = None
    score = 0

    def __init__(self, board, initial_y=None, initial_x=None, final_y=None, final_x=None):
        self.initial_y, self.initial_x, self.final_y, self.final_x = initial_y, initial_x, final_y, final_x
        self.board = board
        self.children = []
        self.evaluate()

    def generate_children(self, player):
        for y in range(0, 8):
            for x in range(0, 8):
                if self.board[y][x] != EMPTY_STATE:
                    if player == AI and self.board[y][x].islower():
                        iteration_moves = Movement.get_moves(self.board, self.board[y][x], x, y)
                        for next_y, next_x in iteration_moves:
                            new_board = deepcopy(self.board)

                            # swap
                            piece = new_board[y][x]
                            new_board[y][x] = EMPTY_STATE
                            new_board[next_y][next_x] = piece

                            self.children.append(State(new_board, y, Movement.letters[x], next_y, Movement.letters[next_x]))
                    elif player == HUMAN and self.board[y][x].isupper():
                        iteration_moves = Movement.get_moves(self.board, self.board[y][x], x, y)
                        for next_y, next_x in iteration_moves:
                            new_board = deepcopy(self.board)

                            # swap
                            piece = new_board[y][x]
                            new_board[y][x] = EMPTY_STATE
                            new_board[next_y][next_x] = piece

                            self.children.append(
                                State(new_board, y, Movement.letters[x], next_y, Movement.letters[next_x]))

    def evaluate(self):
        if len(self.board) == 0:
            self.score = 0
        else:
            self.score += self.material()

    def material(self):
        score = 0
        piece_values = {'p': 1, 'b': 3, 'n': 3, 'r': 5, 'q': 9, 'k': 90}

        for y in range(0, 8):
            for x in range(0, 8):
                piece = self.board[y][x]
                if piece is not EMPTY_STATE:
                    if piece.islower():
                        score += piece_values[piece]
                    elif piece.isupper():
                        score -= piece_values[piece.lower()]

        return score

    def print_state(self):
        count = 7
        print('\n Score:\t' + str(self.score))
        for y in range(7, -1, -1):
            line = str(count) + '  '
            count -= 1
            for x in range(8):
                line += ' ' + self.board[y][x]
            print(line)
        print('\n    A B C D E F G H\n')