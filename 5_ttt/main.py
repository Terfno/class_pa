from common import printB
from common import isFin
import human


def main():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    printB(board)

    # game loop
    for i in range(len(board)):
        if i % 2 == 0:
            board = human.inputPlayer(board, "x")
        else:
            board = human.inputPlayer(board, "o")

        printB(board)
        jadge, winner = isFin(board)
        if jadge:
            print("winner: "+winner)
            return 0

    print("draw")
    return 0


main()
