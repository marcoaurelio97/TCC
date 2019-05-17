EMPTY_STATE = '.'


class Movement:
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    pieces = 'rnbkqpRNBQKP'

    @staticmethod
    def verify_false_coordinates(x_curr, y_curr, x_next, y_next):
        r = range(0, 8)

        if x_curr not in r or y_curr not in r or x_next not in r or y_next not in r:
            return True

        return False

    @staticmethod
    def verify_piece_not_exists( board, x, y):
        piece = board[y][x]

        if Movement.pieces.find(piece) == -1:
            return True

        return False

    @staticmethod
    def verify_pawn_promotion(piece, y_next):  # TODO: pawn promotion
        piece_promotion = piece
        if piece.lower() == 'p' and (y_next == 7 or y_next == 0):
            while True:
                print('\nWhich piece do you want to promote?')
                print('\nR -> Rook\nN -> Knight\nB -> Bishop\nQ -> Queen')
                chosen_piece = input('\nPiece: ')

                try:
                    if chosen_piece.upper() not in ['R', 'N', 'B', 'Q']:
                        raise Exception('Promotion piece invalid!')
                    piece_promotion = chosen_piece
                    break
                except Exception as ex:
                    print(ex)

        return piece_promotion

    @staticmethod
    def get_moves(board, piece, x, y):
        moves = []
        piece_upper = piece.upper()

        if piece_upper == 'P':
            Movement.get_pawn_moves(board, piece, x, y, moves)
        elif piece_upper == 'R':
            Movement.get_rook_moves(board, x, y, moves)
        elif piece_upper == 'N':
            Movement.get_knight_moves(board, x, y, moves)
        elif piece_upper == 'B':
            Movement.get_bishop_moves(board, x, y, moves)
        elif piece_upper == 'K':
            Movement.get_king_moves(board, x, y, moves)
        elif piece_upper == 'Q':
            Movement.get_queen_moves(board, x, y, moves)

        return moves

    @staticmethod
    def get_pawn_moves( board, piece, x, y, moves):
        if piece.isupper():
            if y < 7 and board[y + 1][x] == EMPTY_STATE:
                moves.append([y + 1, x])
            if y == 1 and board[y + 1][x] == EMPTY_STATE and board[y + 2][x] == EMPTY_STATE:
                moves.append([y + 2, x])
            if x < 7 and y < 7 and board[y + 1][x + 1] != EMPTY_STATE and board[y + 1][x + 1].islower():
                moves.append([y + 1, x + 1])
            if x > 0 and y < 7 and board[y + 1][x - 1] != EMPTY_STATE and board[y + 1][x - 1].islower():
                moves.append([y + 1, x - 1])
        else:
            if y > 0 and board[y - 1][x] == EMPTY_STATE:
                moves.append([y - 1, x])
            if y == 6 and board[y - 1][x] == EMPTY_STATE and board[y - 2][x] == EMPTY_STATE:
                moves.append([y - 2, x])
            if x > 0 and y > 0 and board[y - 1][x - 1] != EMPTY_STATE and board[y - 1][x - 1].isupper():
                moves.append([y - 1, x - 1])
            if x < 7 and y > 0 and board[y - 1][x + 1] != EMPTY_STATE and board[y - 1][x + 1].isupper():
                moves.append([y - 1, x + 1])

    @staticmethod
    def get_rook_moves( board, x, y, moves):
        up = down = right = left = True
        for i in range(1, 8):
            if up and y + i < 8:
                if board[y + i][x] != EMPTY_STATE:
                    if Movement.check_team(board, x, y, x, y + i):
                        moves.append([y + i, x])
                    up = False
                else:
                    moves.append([y + i, x])

            if down and y - i >= 0:
                if board[y - i][x] != EMPTY_STATE:
                    if Movement.check_team(board, x, y, x, y - i):
                        moves.append([y - i, x])
                    down = False
                else:
                    moves.append([y - i, x])

            if right and x + i < 8:
                if board[y][x + i] != EMPTY_STATE:
                    if Movement.check_team(board, x, y, x + i, y):
                        moves.append([y, x + i])
                    right = False
                else:
                    moves.append([y, x + i])

            if left and x - i >= 0:
                if board[y][x - i] != EMPTY_STATE:
                    if Movement.check_team(board, x, y, x - i, y):
                        moves.append([y, x - i])
                    left = False
                else:
                    moves.append([y, x - i])

    @staticmethod
    def get_knight_moves(board, x, y, moves):
        if 0 <= y + 1 < 8 and 0 <= x + 2 < 8 and Movement.check_team(board, x, y, x + 2, y + 1):
            moves.append([y + 1, x + 2])
        if 0 <= y - 1 < 8 and 0 <= x + 2 < 8 and Movement.check_team(board, x, y, x + 2, y - 1):
            moves.append([y - 1, x + 2])
        if 0 <= y + 2 < 8 and 0 <= x + 1 < 8 and Movement.check_team(board, x, y, x + 1, y + 2):
            moves.append([y + 2, x + 1])
        if 0 <= y - 2 < 8 and 0 <= x + 1 < 8 and Movement.check_team(board, x, y, x + 1, y - 2):
            moves.append([y - 2, x + 1])
        if 0 <= y - 1 < 8 and 0 <= x - 2 < 8 and Movement.check_team(board, x, y, x - 2, y - 1):
            moves.append([y - 1, x - 2])
        if 0 <= y + 1 < 8 and 0 <= x - 2 < 8 and Movement.check_team(board, x, y, x - 2, y + 1):
            moves.append([y + 1, x - 2])
        if 0 <= y + 2 < 8 and 0 <= x - 1 < 8 and Movement.check_team(board, x, y, x - 1, y + 2):
            moves.append([y + 2, x - 1])
        if 0 <= y - 2 < 8 and 0 <= x - 1 < 8 and Movement.check_team(board, x, y, x - 1, y - 2):
            moves.append([y - 2, x - 1])

    @staticmethod
    def check_team(board, x_curr, y_curr, x_next, y_next):
        piece_curr = board[y_curr][x_curr]
        piece_next = board[y_next][x_next]

        if piece_next == EMPTY_STATE:
            return True
        if piece_curr.isupper() == piece_next.isupper():
            return False
        elif piece_curr.islower() == piece_next.islower():
            return False
        else:
            return True

    @staticmethod
    def get_bishop_moves( board, x, y, moves):
        up_right = up_left = down_right = down_left = True

        for i in range(1, 8):
            if up_right and y + i < 8 and x + i < 8:
                if board[y + i][x + i] != EMPTY_STATE:
                    if Movement.check_team(board, x, y, x + i, y + i):
                        moves.append([y + i, x + i])
                    up_right = False
                else:
                    moves.append([y + i, x + i])
            if up_left and y - i >= 0 and x + i < 8:
                if board[y - i][x + i] != EMPTY_STATE:
                    if Movement.check_team(board, x, y, x + i, y - i):
                        moves.append([y - i, x + i])
                    up_left = False
                else:
                    moves.append([y - i, x + i])
            if down_right and y + i < 8 and x - i >= 0:
                if board[y + i][x - i] != EMPTY_STATE:
                    if Movement.check_team(board, x, y, x - i, y + i):
                        moves.append([y + i, x - i])
                    down_right = False
                else:
                    moves.append([y + i, x - i])
            if down_left and y - i >= 0 and x - i >= 0:
                if board[y - i][x - i] != EMPTY_STATE:
                    if Movement.check_team(board, x, y, x - i, y - i):
                        moves.append([y - i, x - i])
                    down_left = False
                else:
                    moves.append([y - i, x - i])

    @staticmethod
    def get_queen_moves(board, x, y, moves):
        Movement.get_rook_moves(board, x, y, moves)
        Movement.get_bishop_moves(board, x, y, moves)

    @staticmethod
    def get_king_moves(board, x, y, moves):
        if 0 <= y + 1 < 8 and 0 <= x - 1 < 8 and Movement.check_team(board, x, y, x - 1, y + 1):
            moves.append([y + 1, x - 1])
        if 0 <= y + 1 < 8 and 0 <= x < 8 and Movement.check_team(board, x, y, x, y + 1):
            moves.append([y + 1, x])
        if 0 <= y + 1 < 8 and 0 <= x + 1 < 8 and Movement.check_team(board, x, y, x + 1, y + 1):
            moves.append([y + 1, x + 1])
        if 0 <= y < 8 and 0 <= x - 1 < 8 and Movement.check_team(board, x, y, x - 1, y):
            moves.append([y, x - 1])
        if 0 <= y < 8 and 0 <= x + 1 < 8 and Movement.check_team(board, x, y, x + 1, y):
            moves.append([y, x + 1])
        if 0 <= y - 1 < 8 and 0 <= x - 1 < 8 and Movement.check_team(board, x, y, x - 1, y - 1):
            moves.append([y - 1, x - 1])
        if 0 <= y - 1 < 8 and 0 <= x < 8 and Movement.check_team(board, x, y, x, y - 1):
            moves.append([y - 1, x])
        if 0 <= y - 1 < 8 and 0 <= x + 1 < 8 and Movement.check_team(board, x, y, x + 1, y - 1):
            moves.append([y - 1, x + 1])
