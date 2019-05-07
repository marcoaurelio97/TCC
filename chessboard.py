import numpy as np

EMPTY_STATE = '.'


class Chessboard:
    board = np.array([])
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    pieces = 'rnbkqpRNBQKP'

    def __init__(self):
        self.initial_state()

    def initial_state(self):
        self.board = np.array([
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'k', 'q', 'b', 'n', 'r']
        ])

    def print_board(self):
        # cls()
        count = 7
        for y in range(7, -1, -1):
            line = str(count) + '  '
            count -= 1
            for x in range(8):
                line += ' ' + self.board[y][x]
            print(line)
        print('\n    A B C D E F G H\n')

    def move(self, x_curr, y_curr, x_next, y_next):
        x_curr = self.letters.index(x_curr)
        x_next = self.letters.index(x_next)
        piece = self.board[y_curr][x_curr]

        if self.verify_false_coordinates(x_curr, y_curr, x_next, y_next):
            raise Exception('\nInvalid moviment!\n')

        if self.verify_piece_not_exists(x_curr, y_curr):
            raise Exception('\nInvalid moviment!\n')

        moves = self.get_moves(piece, x_curr, y_curr)
        print(moves)

        if [y_next, x_next] not in moves:
            raise Exception('\nInvalid moviment!\n')

        self.board[y_next][x_next] = piece
        self.board[y_curr][x_curr] = EMPTY_STATE

    def verify_false_coordinates(self, x_curr, y_curr, x_next, y_next):
        r = range(0, 8)

        if x_curr not in r or y_curr not in r or x_next not in r or y_next not in r:
            return True

        return False

    def verify_piece_not_exists(self, x, y):
        piece = self.board[y][x]

        if self.pieces.find(piece) == -1:
            return True

        return False

    def get_moves(self, piece, x, y):
        moves = []
        piece_upper = piece.upper()

        if piece_upper == 'P':  # TODO: pawn moves (OK)
            self.get_pawn_moves(piece, x, y, moves)
        elif piece_upper == 'R':  # TODO: rook moves (OK)
            self.get_rook_moves(piece, x, y, moves)
        elif piece_upper == 'N':  # TODO: knight moves (OK)
            self.get_knight_moves(x, y, moves)
        elif piece_upper == 'B':  # TODO: bishop moves
            self.get_bishop_moves(x, y, moves)
        elif piece_upper == 'K':  # TODO: king moves
            self.get_king_moves(x, y, moves)
        elif piece_upper == 'Q':  # TODO: queen moves
            self.get_queen_moves(x, y, moves)

        return moves

    def get_pawn_moves(self, piece, x, y, moves):
        if piece.isupper():
            if y < 7 and self.board[y + 1][x] == EMPTY_STATE:
                moves.append([y + 1, x])
            if y == 1 and self.board[y + 1][x] == EMPTY_STATE and self.board[y + 2][x] == EMPTY_STATE:
                moves.append([y + 2, x])
            if x < 7 and y < 7 and self.board[y + 1][x + 1] != EMPTY_STATE and self.board[y + 1][x + 1].islower():
                moves.append([y + 1, x + 1])
            if x > 0 and y < 7 and self.board[y + 1][x - 1] != EMPTY_STATE and self.board[y + 1][x - 1].islower():
                moves.append([y + 1, x - 1])
        else:
            if y > 0 and self.board[y - 1][x] == EMPTY_STATE:
                moves.append([y - 1, x])
            if y == 6 and self.board[y - 1][x] == EMPTY_STATE and self.board[y - 2][x] == EMPTY_STATE:
                moves.append([y - 2, x])
            if x > 0 and y > 0 and self.board[y - 1][x - 1] != EMPTY_STATE and self.board[y - 1][x - 1].isupper():
                moves.append([y - 1, x - 1])
            if x < 7 and y > 0 and self.board[y - 1][x + 1] != EMPTY_STATE and self.board[y - 1][x + 1].isupper():
                moves.append([y - 1, x + 1])

    def get_rook_moves(self, piece, x, y, moves):
        up = down = right = left = True
        for i in range(1, 8):
            if piece.isupper():
                if up and y + i < 8:
                    if self.board[y + i][x] != EMPTY_STATE:
                        if self.board[y + i][x].islower():
                            moves.append([y + i, x])
                        up = False
                    else:
                        moves.append([y + i, x])

                if down and y - i >= 0:
                    if self.board[y - i][x] != EMPTY_STATE:
                        if self.board[y - i][x].islower():
                            moves.append([y - i, x])
                        down = False
                    else:
                        moves.append([y - i, x])

                if right and x + i < 8:
                    if self.board[y][x + i] != EMPTY_STATE:
                        if self.board[y][x + i].islower():
                            moves.append([y, x + i])
                        right = False
                    else:
                        moves.append([y, x + i])

                if left and x - i >= 0:
                    if self.board[y][x - i] != EMPTY_STATE:
                        if self.board[y][x - i].islower():
                            moves.append([y, x - i])
                        left = False
                    else:
                        moves.append([y, x - i])
            else:
                if up and y - i >= 0:
                    if self.board[y - i][x] != EMPTY_STATE:
                        if self.board[y - i][x].isupper():
                            moves.append([y - i, x])
                        up = False
                    else:
                        moves.append([y - i, x])

                if down and y + i < 8:
                    if self.board[y + i][x] != EMPTY_STATE:
                        if self.board[y + i][x].isupper():
                            moves.append([y + i, x])
                        down = False
                    else:
                        moves.append([y + i, x])

                if right and x - i >= 0:
                    if self.board[y][x - i] != EMPTY_STATE:
                        if self.board[y][x - i].isupper():
                            moves.append([y, x - i])
                        right = False
                    else:
                        moves.append([y, x - i])

                if left and x + i < 8:
                    if self.board[y][x + i] != EMPTY_STATE:
                        if self.board[y][x + i].isupper():
                            moves.append([y, x + i])
                        left = False
                    else:
                        moves.append([y, x + i])

    def get_knight_moves(self, x, y, moves):
        if 0 <= y + 1 < 8 and 0 <= x + 2 < 8 and self.check_team(x, y, x + 2, y + 1):
            moves.append([y + 1, x + 2])
        if 0 <= y - 1 < 8 and 0 <= x + 2 < 8 and self.check_team(x, y, x + 2, y - 1):
            moves.append([y - 1, x + 2])
        if 0 <= y + 2 < 8 and 0 <= x + 1 < 8 and self.check_team(x, y, x + 1, y + 2):
            moves.append([y + 2, x + 1])
        if 0 <= y - 2 < 8 and 0 <= x + 1 < 8 and self.check_team(x, y, x + 1, y - 2):
            moves.append([y - 2, x + 1])
        if 0 <= y - 1 < 8 and 0 <= x - 2 < 8 and self.check_team(x, y, x - 2, y - 1):
            moves.append([y - 1, x - 2])
        if 0 <= y + 1 < 8 and 0 <= x - 2 < 8 and self.check_team(x, y, x - 2, y + 1):
            moves.append([y + 1, x - 2])
        if 0 <= y + 2 < 8 and 0 <= x - 1 < 8 and self.check_team(x, y, x - 1, y + 2):
            moves.append([y + 2, x - 1])
        if 0 <= y - 2 < 8 and 0 <= x - 1 < 8 and self.check_team(x, y, x - 1, y - 2):
            moves.append([y - 2, x - 1])

    def check_team(self, x_curr, y_curr, x_next, y_next):
        piece_curr = self.board[y_curr][x_curr]
        piece_next = self.board[y_next][x_next]

        if piece_next == EMPTY_STATE:
            return True
        if piece_curr.isupper() == piece_next.isupper():
            return False
        elif piece_curr.islower() == piece_next.islower():
            return False
        else:
            return True

    def get_bishop_moves(self, x, y, moves):
        for i in range(8):
            if 0 <= y + i < 8 and 0 <= x + i < 8 and self.check_team(x, y, x + i, y + i):
                moves.append([y + i, x + i])
            if 0 <= y - i < 8 and 0 <= x + i < 8 and self.check_team(x, y, x + i, y - i):
                moves.append([y - i, x + i])
            if 0 <= y + i < 8 and 0 <= x - i < 8 and self.check_team(x, y, x - i, y + i):
                moves.append([y + i, x - i])
            if 0 <= y - i < 8 and 0 <= x - i < 8 and self.check_team(x, y, x - i, y - i):
                moves.append([y - i, x - i])

    def get_queen_moves(self, x, y, moves):
        self.get_rook_moves(x, y, moves)
        self.get_bishop_moves(x, y, moves)

    def get_king_moves(self, x, y, moves):
        if 0 <= y + 1 < 8 and 0 <= x - 1 < 8 and self.check_team(x, y, x - 1, y + 1):
            moves.append([y + 1, x - 1])
        if 0 <= y + 1 < 8 and 0 <= x < 8 and self.check_team(x, y, x, y + 1):
            moves.append([y + 1, x])
        if 0 <= y + 1 < 8 and 0 <= x + 1 < 8 and self.check_team(x, y, x + 1, y + 1):
            moves.append([y + 1, x + 1])
        if 0 <= y < 8 and 0 <= x - 1 < 8 and self.check_team(x, y, x - 1, y):
            moves.append([y, x - 1])
        if 0 <= y < 8 and 0 <= x + 1 < 8 and self.check_team(x, y, x + 1, y):
            moves.append([y, x + 1])
        if 0 <= y - 1 < 8 and 0 <= x - 1 < 8 and self.check_team(x, y, x - 1, y - 1):
            moves.append([y - 1, x - 1])
        if 0 <= y - 1 < 8 and 0 <= x < 8 and self.check_team(x, y, x, y - 1):
            moves.append([y - 1, x])
        if 0 <= y - 1 < 8 and 0 <= x + 1 < 8 and self.check_team(x, y, x + 1, y - 1):
            moves.append([y - 1, x + 1])
