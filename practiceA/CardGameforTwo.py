# 問題　https://atcoder.jp/contests/abs/tasks/abc088_b

# 自分の回答
import math
n = int(input())
cards = list(map(int,input().split()))

cards.sort()

alice = 0
bob = 0

for card in range(math.ceil(len(cards)/2)):
    alice += cards.pop()
    if cards:
        bob += cards.pop()

print(alice - bob)

# 他回答例
# input関数をint関数で囲み、整数値として変数Nに設定
N = int(input())
# input().split()で空白区切りの文字列を取得 → intに変換 → list関数で囲み、リストとしてaに設定
a = list(map(int, input().split()))
# sortメソッドの引数にreverse=Trueを設定し、リストを降順に並べ替える
a.sort(reverse=True)
# スライスを[0::2]と設定し、リストの偶数番目を取得
Alice_calds = a[0::2]
# スライスを[1::2]と設定し、リストの奇数番目を取得
Bob_calds = a[1::2]
# sum関数でそれぞれの合計値を求め、Aliceの合計値からBobの合計値を引く
ans = sum(Alice_calds)-sum(Bob_calds)
# print関数で結果を表示
print(ans)