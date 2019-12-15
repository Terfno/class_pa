import random
import common


# get empty frame sub and return list of the sub
def getEmpty(board):
    emp = []
    for i in range(len(board)):
        if board[i] != "x" or board[i] != "o":
            emp.append(i)

    return emp


# input for random
def inputRandom(board, symbol):
    availableFrame = getEmpty(board)
    code = availableFrame[random.randint(0, len(availableFrame))]

    return common.inputPlayer(
        board, symbol, code)
