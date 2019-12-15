import common


# input for human
def inputHuman(board, symbol):
    player = int(
        input("\n> Where would you like to put your symbol '" + symbol + "'? : "))
    print("")
    code = player-1

    return common.inputPlayer(board, symbol, code)
