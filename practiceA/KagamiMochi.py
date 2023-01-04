# 問題：https://atcoder.jp/contests/abs/tasks/abc085_b

# 自分の回答例
n = int(input())
mochies = []

for i in range(n):
    mochies.append(int(input()))

distinct_mochies = list(set(mochies))

print(len(distinct_mochies))

# ほかの回答例
N = int(input())
d = [input() for _ in range(N)]
print(len(set(d)))