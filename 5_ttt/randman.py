import random
import common


# get empty frame sub and return list of the sub
def getEmpty(board):
    emp = []
    for i in range(len(board)):
        if board[i] == "x" or board[i] == "o":
            continue
        else:
            emp.append(i)

    return emp


# input for random
def inputer(board, symbol):
    availableFrame = getEmpty(board)
    code = availableFrame[random.randint(0, len(availableFrame) - 1)]

    print("randman> I put at " + str(code+1))
    print("")

    return common.inputPlayer(
        board, symbol, code)
