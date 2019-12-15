import numpy


def createQTable(board):
    columns = len(board)
    rows = 3**len(board)
    return numpy.zeros((rows, columns))


def recordB(board, blog, code):
    record = [board, code]
    blog.append(record)
    return blog


def updateTable(qTable, blog, win):
    for i in range(len(blog)):
        board = blog[i][0]
        column = blog[i][1]
        row = findRow(board)
        if win==1:
            qTable[row, column] += 2
        elif win==2:
            qTable[row, column] -= 2
        else:
            qTable[row, column] += 1

    return qTable


def findRow(board):
    index = 0
    for i in range(len(board)):
        if board[i] == "o":
            coef = 1
        elif board[i] == "x":
            coef = 2
        else:
            coef = 0
        index += (3**i)*coef
    return index
