import requests
import json

EMPTY_STATE = '.'


def get_player_move(curr_board):
    print(curr_board)
    # pos = input('Enter the current and next position of the piece: ')
    # pos_split = pos.split(' ')
    #
    # if len(pos) != 5 or len(pos_split) != 2:
    #     raise Exception('Invalid positions!')
    #
    # x_curr = pos_split[0][0].upper()
    # y_curr = int(pos_split[0][1])
    # x_next = pos_split[1][0].upper()
    # y_next = int(pos_split[1][1])

    url = "https://tcc-xadrez.firebaseio.com/board.json"
    r = requests.get(url)
    next_board = json.loads(r.content)
    print(next_board)

    # for y in range(7, -1, -1):
    #     line = str(count) + '  '
    #     count -= 1
    #     for x in range(8):
    #         line += ' ' + self.board[y][x]
    #     print(line)
    count = 0
    for y in range(0, 8):
        for x in range(0, 8):
            if curr_board[y][x] != EMPTY_STATE and next_board[y][x] != 0:
                count += 1

    print(count)
    # return y_curr, x_curr, y_next, x_next
