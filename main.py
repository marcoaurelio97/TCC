from game import *


def main():
    op = input("1 - AI vs AI\n2 - Player vs AI\n")
    game = Game(op)
    game.run()


if __name__ == '__main__':
    main()
