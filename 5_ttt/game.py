import common
import human
import randman


def gameLoop():
    # select for first attacker and second attacker
    fp = common.xSelect()
    sp = common.oSelect()

    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    common.printB(board)

    # game loop
    for i in range(len(board)):
        if i % 2 == 0:
            if fp == 1:
                human.inputHuman(board, "x")
            elif fp == 2:
                randman.inputRandom(board, "x")
        else:
            if sp == 1:
                randman.inputRandom(board, "o")
            elif sp == 2:
                randman.inputRandom(board, "o")

        common.printB(board)
        if common.isFin(board):
            return 0

    print("draw")
    return 0


def main():
    gameLoop()


main()
