# 問題：https://atcoder.jp/contests/abs/tasks/abc085_c

n,price = map(int,input().split())
print(n)
print(price)

# 0~Nまで順番に変数i(10000円の枚数)に設定
for i in range(n+1):
    # 0~N-iまで順番に変数j(5000円の枚数)に設定※N-iはj(5000円の枚数)の考えうる最大値
    for j in range(n-i+1):
        # iとjからkの枚数が決定する
        k = n - i - j
        # 合計金額と比較し、等しくなる場合
        if i*10000 + j*5000 + k*1000 == price:
            # それぞれの枚数を表示
            print(f"{i} {j} {k} ")
            exit()
# 一つも候補がない場合、-1, -1, -1を表示する
print("-1 -1 -1")
