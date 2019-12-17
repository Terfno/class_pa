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
xqTable = learn.createQTable(9)
oqTable = learn.createQTable(9)


def gameloop(fp, sp, mode):
    global xwin
    global owin
    global draw
    global xqTable
    global oqTable

    # print("new game!")
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if mode == 0:
        common.printB(board)

    xblog = []
    oblog = []

    # game loop
    for i in range(len(board)):
        if i % 2 == 0:
            if fp == 3:
                code = ai.codeAINP(board, xqTable)
                board = common.inputPlayer(board, "x", code)
                xblog = learn.recordB(board, xblog, code)
            else:
                board = common.inputer(board, "x", fp)
        else:
            if sp == 3:
                code = ai.codeAINP(board, oqTable)
                board = common.inputPlayer(board, "o", code)
                oblog = learn.recordB(board, oblog, code)
            else:
                board = common.inputer(board, "o", sp)

        if mode == 0:
            common.printB(board)

        jadge = common.isFinNP(board)
        if jadge == "x":
            xqTable = learn.updateTable(xqTable, xblog, 1)
            oqTable = learn.updateTable(oqTable, oblog, 2)
            xwin += 1
            return 0
        elif jadge == "o":
            oqTable = learn.updateTable(oqTable, oblog, 1)
            xqTable = learn.updateTable(xqTable, xblog, 2)
            owin += 1
            return 0

    xqTable = learn.updateTable(xqTable, xblog, 3)
    oqTable = learn.updateTable(oqTable, oblog, 3)
    draw += 1
    return 0


def main():
    global xwin
    global owin
    global draw
    global xqTable
    global oqTable

    # select for first attacker and second attacker
    fp = 3  # common.xSelect()
    sp = 3  # common.oSelect()

    lt = 100000

    for i in tqdm(range(lt)):
        gameloop(fp, sp, 1)

    # for i in range(lt):
    #     fp = common.xSelect()
    #     sp = common.oSelect()
    #     gameloop(fp, sp, 0)

    numpy.set_printoptions(threshold=numpy.inf)
    print(xqTable)
    print("xwin: " + str(xwin))
    print("owin: " + str(owin))
    print("draw: " + str(draw))


main()
