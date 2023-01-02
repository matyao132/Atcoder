# 問題　https://atcoder.jp/contests/abs/tasks/abc081_b

n = int(input())
list_a = list(map(int,input().split()))

flag = 0
count = 0

while True:
    for i in range(n):
        if list_a[i] %2 != 0:
            flag = 1
            break

    if flag == 1:
        break

    count += 1

    for i in range(n):
        list_a[i] = list_a[i] / 2

print(count)