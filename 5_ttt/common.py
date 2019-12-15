import math
import human
import randman


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


# input to board with symbol and code
def inputPlayer(board, symbol, code):
    board[code] = symbol
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
            return "x"
        elif len(oset) == 3:
            print("> win o player!")
            return "o"

    return False


# player select for First
def xSelect():
    select = input(
        "\n> Which would you like to play for first attack?\n1:Human(You or your friend), 2:Random or 3:AI(not available): ")
    return int(select)


# player select for Second
def oSelect():
    select = input(
        "\n> Which would you like to play for second attack?\n1:Human(You or your friend), 2:Random or 3:AI(not available): ")
    return int(select)


# input with select
def inputer(board, symbol, id):
    if id == 1:
        human.inputer(board, symbol)
    elif id == 2:
        randman.inputer(board, symbol)
