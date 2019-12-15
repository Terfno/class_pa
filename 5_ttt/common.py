import math


# printing board
def printB(board):
    width = int(math.sqrt(len(board)))
    for i in range(len(board)):
        if i+1 == len(board):
            print(str(board[i]))
            continue
        if (i+1) % (width) == 0:
            print(str(board[i]))
            print("---------")
        else:
            print(str(board[i])+" | ", end="")
    print("")
    return


# get input from human player and apply game board
def inputPlayer(board, symbol):
    player = int(
        input("\n> where would you like to put your symbol '" + symbol + "' : "))
    print("")
    board[player-1] = symbol
    return board


# judgement of win
def isFin(board):
    xsub = []
    osub = []
    win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
           [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for i in range(len(board)):
        if board[i] == "x":
            xsub.append(i)
        elif board[i] == "o":
            osub.append(i)

    for i in range(len(win)):
        xset = []
        oset = []
        xset = list(set(xsub) & set(win[i]))
        oset = list(set(osub) & set(win[i]))

        if len(xset) == 3:
            print("> win x player!")
            return True
        elif len(oset) == 3:
            print("> win o player!")
            return True

    return False
