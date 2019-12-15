import common
import learn
import randman
import random


def codeAINP(board, qTable):
    emp = randman.getEmpty(board)
    index = learn.findRow(board)
    base = qTable[index]
    opt = []

    for i in range(len(emp)):
        opt.append(base[emp[i]])

    cache = 0
    code = 0
    for i in range(len(opt)):
        if opt[i] > cache:
            code = i
        elif opt[i] == cache and random.randint(0, 1) == 0:
            code = i

    if random.randint(0,5)==0:
        return emp[random.randrange(0,len(emp))]
    else:
        return emp[code]


def codeAI(board, qTable):
    emp = randman.getEmpty(board)
    index = learn.findRow(board)
    base = qTable[index]
    opt = []

    for i in range(len(emp)):
        opt.append(base[emp[i]])

    cache = 0
    code = 0
    for i in range(len(opt)):
        if opt[i] > cache:
            code = i

    print("AI> i put at "+str(emp[i]+1))
    return emp[i]
