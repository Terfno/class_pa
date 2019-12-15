# get empty frame sub and return list of the sub
def getEmpty(board):
    emp = []
    for i in range(len(board)):
        if board[i] != "x" or board[i] != "o":
            emp.append(i)
    
    return emp

