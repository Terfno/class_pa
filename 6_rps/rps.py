# ref: https://core.ac.uk/download/pdf/61354812.pdf

import random
# (g:rock,p:paper,t:scissors)


def hand_random(hands):  # でたらめ戦法
    r = random.randrange(0, 3)
    return hands[r]


def hand_one(hands, n):  # 一筋戦法-n
    return hands[n]


def hand_copy(past, n):  # ものまね-n手前
    return past[len(past) - 1 - n]


def hand_if(hands, jadged):  # 場合分け戦略
    return hands[jadge]  # draw:0->rock, lose:1->paper, win:2->scissors


def jadge(my, enemy):  # 判定
    if my == enemy:  # draw
        return 0
    elif (my == "g" and enemy == "p") or (my == "p" and enemy == "t") or (my == "t" and enemy == "g"):  # lose
        return 1
    elif (my == "g" and enemy == "t") or (my == "p" and enemy == "g") or (my == "t" and enemy == "p"):  # win
        return 2


def add_point(jadge, point):  # ポイント加算
    add = [5, -3, 2]  # [draw, lose, win]
    return point + add[jadge]


def main():
    # times = int(input("How many times do you play?:"))
    hands = ["g", "p", "t"]

    past = []
    jadged = 0

    times = 10
    point = 0

    for _ in range(times):
        myHand = hand_random(hands)
        print("myhand:" + myHand)
        enemyHand = input("Enemy's Hand(g:rock,p:paper,t:scissors): ")
        past.append(enemyHand)
        jadged = jadge(myHand, enemyHand)
        point = add_point(jadge, point)

    print(point)


main()
