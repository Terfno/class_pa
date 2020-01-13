# (g:rock,p:paper,t:scissors)
# # ref: https://core.ac.uk/download/pdf/61354812.pdf

import random
import numpy
import copy

Pattern = numpy.zeros(3**3, 3)  # 履歴2戦略用のテーブル


def hand_random(hands):  # でたらめ戦略
    r = random.randrange(0, len(hands))
    return hands[r]


def hand_one(hands, n):  # 一筋n戦略
    return hands[n]


def hand_copy(past, n):  # n手前ものまね戦略
    return past[len(past) - 1 - n]


def hand_if(hands, jadged):  # 場合分け戦略
    return hands[jadge]  # draw:0->rock, lose:1->paper, win:2->scissors


def hand_hist(st, hands):  # 履歴2戦略
    global Pattern

    if len(st) == 3:  # patternの更新
        index = find_row(st)
        Pattern[index] += 1
        _ = st.pop()

    if len(st) == 2:  # 履歴2戦略ロジック部分
        should = [
            Pattern[find_row(st.append("g"))],
            Pattern[find_row(st.append("p"))],
            Pattern[find_row(st.append("t"))]
        ]
        return hands[should.index(max(should))]
    elif len(st) < 2:  # 履歴が足りないときはランダム
        return hand_random(hands)


def find_row(past_t):  # 行特定->三進数から十進数への変換してるだけ
    index = 0
    for i in range(past_t):
        if past_t[i] == "g":
            coef = 0
        elif past_t[i] == "p":
            coef = 1
        elif past_t[i] == "t":
            coef = 2
        index += (3**i)*coef
    return index


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
    global Pattern
    # times = int(input("How many times do you play?:"))
    hands = ["g", "p", "t"]

    past = []  # 過去手
    jadged = 0  # 今回の判定 0,1,2
    past_t = []  # 過去3手 履歴2戦略用

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
