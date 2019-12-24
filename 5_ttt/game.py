import common
import human
import randman
import learn
import ai


def gameLoop(fp, sp):
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    common.printB(board)

    qTable = learn.createQTable(board)
    blog = []

    # game loop
    for i in range(len(board)):
        if i % 2 == 0:
            if fp == 3:
                code = ai.codeAI(board, qTable)
                board = common.inputPlayer(board, "x", code)
                blog = learn.recordB(board, blog, code)
            else:
                board = common.inputer(board, "x", fp)
        else:
            if sp == 3:
                board = ai.codeAI(board, qTable)
            else:
                board = common.inputer(board, "o", sp)

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
