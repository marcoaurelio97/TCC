from Chess.movement_rules import Movement
from Minimax.penalties import Penalties
from copy import deepcopy

EMPTY_STATE = '.'
MINIMAZING_PLAYER = -1
MAXIMAZING_PLAYER = 1


class State:
    initial_y = initial_x = final_y = final_x = None
    board = None
    children = None
    score = 0
    material_score = 0
    square_score = 0
    number_of_moves = 0

    def __init__(self, board, initial_y=None, initial_x=None, final_y=None, final_x=None, player=None):
        self.player_turn = player
        self.initial_y, self.initial_x, self.final_y, self.final_x = initial_y, initial_x, final_y, final_x
        self.board = board
        self.children = []

    def generate_children(self, player):
        for y in range(0, 8):
            for x in range(0, 8):
                if self.board[y][x] != EMPTY_STATE:
                    if player == MINIMAZING_PLAYER and self.board[y][x].islower():
                        iteration_moves = Movement.get_moves(self.board, self.board[y][x], x, y)
                        self.number_of_moves += len(iteration_moves)
                        for next_y, next_x in iteration_moves:
                            new_board = deepcopy(self.board)

                            # swap
                            piece = new_board[y][x]
                            new_board[y][x] = EMPTY_STATE
                            new_board[next_y][next_x] = piece

                            self.children.append(
                                State(new_board, y, Movement.letters[x], next_y, Movement.letters[next_x], player))

                    elif player == MAXIMAZING_PLAYER and self.board[y][x].isupper():
                        iteration_moves = Movement.get_moves(self.board, self.board[y][x], x, y)
                        self.number_of_moves -= len(iteration_moves)
                        for next_y, next_x in iteration_moves:
                            new_board = deepcopy(self.board)

                            # swap
                            piece = new_board[y][x]
                            new_board[y][x] = EMPTY_STATE
                            new_board[next_y][next_x] = piece

                            self.children.append(
                                State(new_board, y, Movement.letters[x], next_y, Movement.letters[next_x], player))

    def get_score(self):
        if len(self.board) == 0:
            self.score = 0
        else:
            self.score += self.material()
            self.score += self.square()

            if len(self.children) > 0:
                self.score += self.number_of_moves
            else:
                self.generate_children(self.player_turn)
                self.score += self.number_of_moves

        return self.score

    def material(self):
        score = 0
        piece_values = {'p': 10, 'b': 30, 'n': 30, 'r': 50, 'q': 90, 'k': 900}

        for y in range(0, 8):
            for x in range(0, 8):
                piece = self.board[y][x]
                if piece is not EMPTY_STATE:
                    if piece.islower():
                        score += piece_values[piece]
                    elif piece.isupper():
                        score -= piece_values[piece.lower()]

        self.material_score = score

        return score

    def square(self):
        score = 0

        for y in range(0, 8):
            for x in range(0, 8):
                piece = self.board[y][x]
                if piece is not EMPTY_STATE:
                    if self.player_turn == MINIMAZING_PLAYER and piece.islower():
                        score += Penalties.get_score_by_piece(piece, x, y)
                    elif self.player_turn == MAXIMAZING_PLAYER and piece.isupper():
                        score += Penalties.get_score_by_piece(piece, x, y)

        self.square_score = score

        return score

    def print_state(self):
        count = 7
        print(
            """\n
            Score: {}\n
            Material: {}\n
            Square: {}\n
            Number of Moves: {}\n
            Player Turn: {}\n
            """.format(self.score, self.material_score, self.square_score, self.number_of_moves, self.player_turn))
        for y in range(7, -1, -1):
            line = str(count) + '  '
            count -= 1
            for x in range(8):
                line += ' ' + self.board[y][x]
            print(line)
        print('\n    A B C D E F G H\n')

    #TODO verificar se o estado é terminal