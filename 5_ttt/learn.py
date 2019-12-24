import numpy


def createQTable(board):
    columns = len(board)
    rows = 3**len(board)
    return numpy.zeros((rows, columns))


def recordB(board, blog, code):
    record = [board, code]
    return blog.append(record)


def updateTable(qTable, blog, win):
    for i in range(len(blog)):
        board = blog[i][0]
        column = blog[i][1]
        row = findRow(board)
        if win:
            qTable[row, column] += 1
        else:
            qTable[row, column] -= 1


def findRow(board):
    index = 0
    for i in range(len(board)):
        if board[i] == "x":
            coef = 1
        elif board[i] == "o":
            coef = 2
        else:
            coef = 0
        index += (3**i)*coef
    return index
