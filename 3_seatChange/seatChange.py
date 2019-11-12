import random


def r_rand():
    r = random.randint(0, 17)
    if(indexList[r] == 30 or indexList[r] == 31 or indexList[r] == 43):
        r = r_rand()
    return r


indexList = list(range(1, 46, 1))
random.shuffle(indexList)

index_eyeBad = []

for i in range(len(indexList)):
    if(indexList[i] == 30):
        index_eyeBad.append(i)
    if(indexList[i] == 31):
        index_eyeBad.append(i)
    if(indexList[i] == 43):
        index_eyeBad.append(i)

for i in index_eyeBad:
    if(i >= 18):
        r = r_rand()
        swap = indexList[i]
        indexList[i] = indexList[r]
        indexList[r] = swap

print("\n\t\t黒板側\n")
for i in range(len(indexList)):
    print(str(indexList[i]) + "\t", end="")
    if((i+1) % 6 == 0):
        print("")
print("\n")
