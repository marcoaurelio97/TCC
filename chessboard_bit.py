class ChessboardBit:
    white_pawns = ''
    white_rooks = ''
    white_knights = ''
    white_bishops = ''
    white_queen = ''
    white_king = ''
    black_pawns = ''
    black_rooks = ''
    black_knights = ''
    black_bishops = ''
    black_queen = ''
    black_king = ''
    all_white_pieces = ''
    all_black_pieces = ''

    def __init__(self):
        self.initial_state()
        self.all_white_pieces()
        self.all_black_pieces()

    def initial_state(self):
        self.white_pawns   = '0000000000000000000000000000000000000000000000001111111100000000'
        self.white_rooks   = '0000000000000000000000000000000000000000000000000000000010000001'
        self.white_knights = '0000000000000000000000000000000000000000000000000000000001000010'
        self.white_bishops = '0000000000000000000000000000000000000000000000000000000000100100'
        self.white_queen   = '0000000000000000000000000000000000000000000000000000000000010000'
        self.white_king    = '0000000000000000000000000000000000000000000000000000000000001000'
        self.black_pawns   = '0000000011111111000000000000000000000000000000000000000000000000'
        self.black_rooks   = '1000000100000000000000000000000000000000000000000000000000000000'
        self.black_knights = '0100001000000000000000000000000000000000000000000000000000000000'
        self.black_bishops = '0010010000000000000000000000000000000000000000000000000000000000'
        self.black_queen   = '0000100000000000000000000000000000000000000000000000000000000000'
        self.black_king    = '0001000000000000000000000000000000000000000000000000000000000000'

    def print_board(self):
        for i in range(64):
            a = 1

    def all_pieces(self):
        a = 1

    def all_white_pieces(self):
        self.all_white_pieces = self.white_pawns | self.white_rooks\
                                | self.white_knights | self.white_bishops\
                                | self.white_queen | self.white_king

    def all_black_pieces(self):
        self.all_black_pieces = self.black_pawns | self.black_rooks \
                                | self.black_knights | self.black_bishops \
                                | self.black_queen | self.black_king
