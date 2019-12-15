import common
import human
import randman


def gameLoop(fp, sp):
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    common.printB(board)

    # game loop
    for i in range(len(board)):
        if i % 2 == 0:
            common.inputer(board, "x", fp)
        else:
            common.inputer(board, "o", sp)

        common.printB(board)

        jadge = common.isFin(board)
        if jadge == "x" or jadge == "o":
            return jadge

    print("draw")
    return "draw"


def main():
    # select for first attacker and second attacker
    fp = common.xSelect()
    sp = common.oSelect()
    gameLoop(fp, sp)


main()
