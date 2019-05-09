from chessboard import *
from functions import *


def main():
    chessboard = Chessboard()

    while True:
        chessboard.print_board()

        x_curr, y_curr, x_next, y_next = get_coordinates()

        if x_curr not in chessboard.letters or x_next not in chessboard.letters:
            raise Exception('\nInvalid positions!\n')

        # cls()

        try:
            chessboard.move(x_curr, y_curr, x_next, y_next)
        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    cls()
    main()
