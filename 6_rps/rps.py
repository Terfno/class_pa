# (g:rock,p:paper,t:scissors)
# # ref: https://core.ac.uk/download/pdf/61354812.pdf

import random
import numpy
import copy

Pattern = [0]*(3**3)  # 履歴2戦略用のテーブル


def hand_hist(hands, st):  # 履歴2戦略
    global Pattern

    if len(st) == 3:  # patternの更新
        index = find_row(st)
        Pattern[index] += 1
        _ = st.pop(0)

    if len(st) == 2:  # 履歴2戦略ロジック部分
        stg = copy.copy(st)
        stg.append('g')
        stp = copy.copy(st)
        stp.append('p')
        stt = copy.copy(st)
        stt.append('t')

        should = [
            Pattern[find_row(stg)],
            Pattern[find_row(stp)],
            Pattern[find_row(stt)]
        ]
        return hands[should.index(max(should))]
    elif len(st) < 2:  # 履歴が足りないときはランダム
        return hand_random(hands)


def find_row(past_t):  # 行特定->三進数から十進数への変換してるだけ
    index = 0
    for i in range(len(past_t)):
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


def update_point(jadged, point):  # ポイント加算
    add = [5, -3, 2]  # [draw, lose, win]
    return point + add[jadged]


def update_count(jadged, counter):
    counter[jadged] += 1
    return counter


def main():
    global Pattern
    # times = int(input("How many times do you play?:"))
    hands = ["g", "p", "t"]

    past = []  # 過去手
    jadged = 0  # 今回の判定 0,1,2
    past_t = []  # 過去3手 履歴2戦略用

    times = 1000
    point = 0

    counter = [0, 0, 0]  # count for draw,lose,win

    for i in range(times):
        myHand = hand_hist(hands, past_t)
        print("myhand:" + myHand)

        enemyHand = input(
            "Enemy's Hand(g:rock,p:paper,t:scissors) or exit(e): ")
        if(enemyHand == "e"):
            print("match time: "+str(i))
            break

        past.append(enemyHand)
        past_t.append(enemyHand)
        jadged = jadge(myHand, enemyHand)

        point = update_point(jadged, point)
        counter = update_count(jadged, counter)

    # result
    print("point: "+str(point))
    print("[draw,lose,win]:"+str(counter))
    print(Pattern)


if __name__ == '__main__':
    main()
