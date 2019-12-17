import common
import learn
import randman
import random

lts = 100000
cnt = 0

def codeAINP(board, qTable):
    global lts
    global cnt

    if cnt < lts/4:
        availableFrame = randman.getEmpty(board)
        code = availableFrame[random.randint(0, len(availableFrame) - 1)]
        return code
    elif cnt > lts/4 and cnt < lts/2:
        if random.randint(0, 10000) % 2 == 0:
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
                elif opt[i] == cache and random.randint(0, 10000) % 2 == 0:
                    code = i

            if random.randint(0, 5) == 0:
                return emp[random.randrange(0, len(emp))]
            else:
                return emp[code]
        else:
            availableFrame = randman.getEmpty(board)
            code = availableFrame[random.randint(0, len(availableFrame) - 1)]
            return code
    else:
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
            elif opt[i] == cache and random.randint(0, 10000) % 2 == 0:
                code = i

        if random.randint(0, 5) == 0:
            return emp[random.randrange(0, len(emp))]
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
