import common
import learn
import randman
import random


def codeAI(board, qTable):
    index = learn.findRow(board)
    opt = qTable[index]

    cache = 0
    code = 0
    for i in range(len(opt)):
        if opt[i] >= cache:
            cache = opt[i]
            code = i

    return code
