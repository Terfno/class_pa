import common
import human
import randman
import learn
import ai
import numpy
from tqdm import tqdm

xwin = 0
owin = 0
draw = 0


def gameloop(qTable, fp, sp):
    global xwin
    global owin
    global draw

    # print("new game!")
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # common.printB(board)

    xblog = []
    oblog = []

    # game loop
    for i in range(len(board)):
        if i % 2 == 0:
            if fp == 3:
                code = ai.codeAINP(board, qTable)
                board = common.inputPlayer(board, "x", code)
                xblog = learn.recordB(board, xblog, code)
            else:
                board = common.inputer(board, "x", fp)
        else:
            if sp == 3:
                code = ai.codeAINP(board, qTable)
                board = common.inputPlayer(board, "o", code)
                oblog = learn.recordB(board, oblog, code)
            else:
                board = common.inputer(board, "o", sp)

        # common.printB(board)

        jadge = common.isFinNP(board)
        if jadge == "x":
            qTable = learn.updateTable(qTable, xblog, 1)
            qTable = learn.updateTable(qTable, oblog, 2)
            xwin += 1
            return qTable
        elif jadge == "o":
            qTable = learn.updateTable(qTable, oblog, 1)
            qTable = learn.updateTable(qTable, xblog, 2)
            owin += 1
            return qTable

    qTable = learn.updateTable(qTable, xblog, 3)
    qTable = learn.updateTable(qTable, oblog, 3)
    draw += 1
    return qTable


def gamewith(qTable, fp, sp):
    global xwin
    global owin
    global draw

    print("new game!")
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    common.printB(board)

    xblog = []
    oblog = []

    # game loop
    for i in range(len(board)):
        if i % 2 == 0:
            if fp == 3:
                code = ai.codeAI(board, qTable)
                board = common.inputPlayer(board, "x", code)
                xblog = learn.recordB(board, xblog, code)
            else:
                board = common.inputer(board, "x", fp)
        else:
            if sp == 3:
                code = ai.codeAI(board, qTable)
                board = common.inputPlayer(board, "o", code)
                oblog = learn.recordB(board, oblog, code)
            else:
                board = common.inputer(board, "o", sp)

        common.printB(board)

        jadge = common.isFin(board)
        if jadge == "x":
            qTable = learn.updateTable(qTable, xblog, 1)
            qTable = learn.updateTable(qTable, oblog, 2)
            xwin += 1
            return qTable
        elif jadge == "o":
            qTable = learn.updateTable(qTable, oblog, 1)
            qTable = learn.updateTable(qTable, xblog, 2)
            owin += 1
            return qTable

    qTable = learn.updateTable(qTable, xblog, 3)
    qTable = learn.updateTable(qTable, oblog, 3)
    print("draw")
    draw += 1
    return qTable


def main():
    global xwin
    global owin
    global draw

    qTable = learn.createQTable(9)

    # select for first attacker and second attacker
    fp = 3  # common.xSelect()
    sp = 3  # common.oSelect()

    lt = 100000

    for i in tqdm(range(lt)):
        qTable = gameloop(qTable, fp, sp)

    print("\n")

    fp = 1
    sp = 3
    qTable = gamewith(qTable, fp, sp)

    fp = 3
    sp = 1
    qTable = gamewith(qTable, fp, sp)

    # numpy.set_printoptions(threshold=numpy.inf)
    print(qTable)
    print("xwin: " + str(xwin))
    print("owin: " + str(owin))
    print("draw: " + str(draw))


main()
