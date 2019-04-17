from chessboard import *


def main():
    chessboard = Chessboard()
    chessboard.print_board()

    while True:
        pos = input('Enter the current and next position of the piece: ')
        pos = pos.split(' ')

        x_curr = pos[0][0]
        y_curr = pos[0][1]
        x_next = pos[1][0]
        y_next = pos[1][1]

        status = chessboard.move(x_curr, y_curr, x_next, y_next)

        if not status:
            print('\nInvalid moviment!\n')

        chessboard.print_board()


if __name__ == '__main__':
    main()
