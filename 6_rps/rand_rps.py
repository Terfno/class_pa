import random
# (g:rock,p:paper,t:scissors)


def generateRand(g, p, t):
    r = random.randrange(0, 3)
    if r == 0:
        return g
    if r == 1:
        return p
    if r == 2:
        return t


def jadge(my, enemy):
    if my == enemy:
        # print("draw")
        return 5
    elif (my == "g" and enemy == "p") or (my == "p" and enemy == "t") or (my == "t" and enemy == "g"):
        # print("I lose")
        return -3
    elif (my == "g" and enemy == "t") or (my == "p" and enemy == "g") or (my == "t" and enemy == "p"):
        # print("I win")
        return 2


def main():
    # times = int(input("How many times do you play?:"))
    times = 10
    point = 0
    for _ in range(times):
        myHand = generateRand("g", "p", "t")
        print(myHand)
        enemyHand = input("Enemy's Hand(g:rock,p:paper,t:scissors): ")
        point += jadge(myHand, enemyHand)

    print(point)


main()
