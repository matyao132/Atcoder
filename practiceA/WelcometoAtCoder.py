from sys import stdin

a = int(stdin.readline().rstrip())
b, c = [int(x) for x in stdin.readline().rstrip().split()]
# mapでもよい
# b,c = map(int,input().split())
text = stdin.readline().rstrip()
print(f"{a+b+c} {text}")
