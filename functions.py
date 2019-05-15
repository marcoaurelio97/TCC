import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_player_move():
    pos = input('Enter the current and next position of the piece: ')
    pos_split = pos.split(' ')

    if len(pos) != 5 or len(pos_split) != 2:
        raise Exception('\nInvalid positions!\n')

    x_curr = pos_split[0][0].upper()
    y_curr = int(pos_split[0][1])
    x_next = pos_split[1][0].upper()
    y_next = int(pos_split[1][1])

    return y_curr, x_curr, y_next, x_next
