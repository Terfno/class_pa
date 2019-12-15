import common
import human


def main():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    common.printB(board)

    # game loop
    for i in range(len(board)):
        if i % 2 == 0:
            human.inputHuman(board, "x")
        else:
            human.inputHuman(board, "o")

        common.printB(board)
        if common.isFin(board):
            return 0

    print("draw")
    return 0


main()
