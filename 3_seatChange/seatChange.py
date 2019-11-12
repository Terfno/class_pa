import random

# 30 31 43

indexList = list(range(1, 46, 1))
random.shuffle(indexList)

index_eyeBad = []  # 30か31か43が入っているindexListの添字

for i in range(len(indexList)):
    if(indexList[i] == 30):
        index_eyeBad.append(i)
    if(indexList[i] == 31):
        index_eyeBad.append(i)
    if(indexList[i] == 43):
        index_eyeBad.append(i)

for i in index_eyeBad:
    if(i >= 18):
        r = random.randint(0, 17)
        swap = indexList[i]
        indexList[i] = indexList[r]
        indexList[r] = swap


l = indexList
for i in range(len(l)):
    if(l[i] == 30):
        print("30は"+str(i))
    if(l[i] == 31):
        print("31は"+str(i))
    if(l[i] == 43):
        print("43は"+str(i))

print(indexList)

