# 三目並べ強化学習
## todo
* [x] 対戦環境作成
* [x] ランダムくん作成
* [ ] 学習用の各種メソッド作成
  * [x] テーブル生成
  * [x] ログ収集
  * [ ] ログをもとにテーブル更新(学習)
  * [ ] テーブルをもとに打つAIくん作成

## env
Python 3.7.5
pip 19.3.1 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)

## package
* numpy
* tqdm

## ref
一部
https://qiita.com/thinking_vecta/items/f5b52311d2c0f6a56dc6#qテーブル

```py
def find_q_row(play_area):
    """
    参照時の状況(state)が参照すべき行番号を計算する関数

    ゲームの状況をあらわすリストを受け取り、行番号を返す
    """
    row_index = 0
    for index in range(len(play_area)):
        if play_area[index] == '○':
            coef = 1
        elif play_area[index] == '×':
            coef = 2
        else:
            coef = 0
        row_index += (3 ** index) * coef
    return row_index
```