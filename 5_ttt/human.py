def inputPlayer(board, symbol):
    player = int(
        input("\n> where would you like to put your symbol '" + symbol + "' : "))
    print("")
    board[player-1] = symbol
    return board
