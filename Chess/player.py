import requests
import json
import numpy as np

EMPTY_STATE = '.'
board_comunication = ""


def get_player_move(curr_board):
    pos = input('Enter the current and next position of the piece: ')
    pos_split = pos.split(' ')

    if len(pos) != 5 or len(pos_split) != 2:
        raise Exception('Invalid positions!')

    x_curr = pos_split[0][0].upper()
    y_curr = int(pos_split[0][1])
    x_next = pos_split[1][0].upper()
    y_next = int(pos_split[1][1])

    return y_curr, x_curr, y_next, x_next


def get_player_move_firebase(curr_board):
    global board_comunication
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    url = "https://tcc-xadrez.firebaseio.com/board.json"

    while True:
        r = requests.get(url)
        next_board = json.loads(r.content)

        if not np.array_equal(next_board, board_comunication):
            board_comunication = next_board
            break

    y_curr, x_curr, y_next, x_next = 0, 0, 0, 0
    for y in range(0, 8):
        for x in range(0, 8):
            if curr_board[y][x] == EMPTY_STATE and next_board[y][x] != 0:
                y_next, x_next = y, letters[x]
            elif curr_board[y][x] != EMPTY_STATE and next_board[y][x] == 0:
                y_curr, x_curr = y, letters[x]

    return y_curr, x_curr, y_next, x_next
