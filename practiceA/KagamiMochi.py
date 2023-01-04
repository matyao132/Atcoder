# 問題：https://atcoder.jp/contests/abs/tasks/abc085_b

n = int(input())
mochies = []

for i in range(n):
    mochies.append(int(input()))

distinct_mochies = list(set(mochies))

print(len(distinct_mochies))