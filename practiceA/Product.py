# 問題文
# シカのAtCoDeerくんは二つの正整数 a,b を見つけました。 a と b の積が偶数か奇数か判定してください。

# 制約
# 1 ≤ a,b ≤ 10000
# a,b は整数
from sys import stdin

a, b = [int(x) for x in stdin.readline().rstrip().split()]

if a * b % 2 == 0:
    print('Even')
else:
    print('Odd')