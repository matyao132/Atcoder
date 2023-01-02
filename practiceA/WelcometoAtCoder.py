# 問題文
# 高橋君はデータの加工が行いたいです。

# 整数 a,b,cと、文字列 s が与えられます。 a+b+c の計算結果と、文字列 s を並べて表示しなさい。

# 制約
# 1≤a,b,c≤1,000
# 1≤∣s∣≤100


from sys import stdin

a = int(stdin.readline().rstrip())
b, c = [int(x) for x in stdin.readline().rstrip().split()]
# mapでもよい
# b,c = map(int,input().split())
text = stdin.readline().rstrip()
print(f"{a+b+c} {text}")
