import common


# input for human
def inputer(board, symbol):
    player = int(
        input("\n> Where would you like to put your symbol '" + symbol + "'? : "))
    print("")
    code = player-1

    return common.inputPlayer(board, symbol, code)
