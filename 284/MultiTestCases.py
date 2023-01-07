n = int(input())
nums = []
for i in range(n):
    c = 0
    x = int(input())
    list_a = map(int, input().split())
    for k in list_a:
        if k % 2 == 1:
            c += 1
    else:
        nums.append(c)
else:
    for i in nums:
        print(i)
