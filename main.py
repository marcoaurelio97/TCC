from chessboard import *


def main():
    chessboard = Chessboard()
    chessboard.print_board()

    while True:
        pos = input('Enter the current and next position of the piece: ')
        pos_split = pos.split(' ')

        if len(pos) != 5 or len(pos_split) != 2:
            print('Invalid positions!')
            continue

        x_curr = pos_split[0][0]
        y_curr = int(pos_split[0][1])
        x_next = pos_split[1][0]
        y_next = int(pos_split[1][1])

        if x_curr not in chessboard.letters or x_next not in chessboard.letters:
            print('Invalid positions!')
            continue

        try:
            chessboard.move(x_curr, y_curr, x_next, y_next)
            chessboard.print_board()
        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    main()
