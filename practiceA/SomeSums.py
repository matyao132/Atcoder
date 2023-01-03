# 問題文　https://atcoder.jp/contests/abs/tasks/abc083_b
n,a,b = map(int,input().split())
sum_list = []

for i in range(1,n+1):
    str_n = str(i)
    check_num = sum(list(map(int,str_n)))

    if check_num >= a and check_num <= b:
        sum_list.append(i)

print(sum(sum_list))