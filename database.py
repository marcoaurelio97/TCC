from pymongo import MongoClient
import numpy as np


class Database:  # sudo service mongod start
    client = None
    db = None

    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client.chessboard

    def get(self, collection, board):
        result = self.db[collection].find_one({"board": self.get_board_string(board)})
        return result

    def insert(self, collection, board, y_curr, x_curr, y_next, x_next):
        self.db[collection].insert_one({
            "board": self.get_board_string(board),
            "y_curr": y_curr,
            "x_curr": x_curr,
            "y_next": y_next,
            "x_next": x_next
        })

    @staticmethod
    def get_board_string(board):
        board_string = ""
        for y in range(0, 8):
            for x in range(0, 8):
                board_string += board[y][x]
        return board_string
