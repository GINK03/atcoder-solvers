N = int(input())
S = input()
X = input()

dp = [set() for i in range(N + 1)]

# 買った時の状態から逆引きすれば良い
dp[N] = set([0])

for i in range(N - 1, -1, -1):
    s = int(S[i])
    for r in range(7):
        # 0を選択しないとき
        p1 = (10 * r + s) % 7 in dp[i + 1]
        # 0を選択するとき
        p2 = (10 * r) % 7 in dp[i + 1]
            
        if X[i] == "T":
            # 前の状態が高橋くんの操作ならば, 自由に選択できるのでどちらが片方が成立していてもよい
            if p1 or p2:
                dp[i].add(r)
        else:
            # 前の状態が青木くんの操作ならば, 自由に選択できないのでどっちを選ばれてもよいように両方成立している必要がある
            if p1 and p2:
                dp[i].add(r)

if 0 in dp[0]:
    print("Takahashi")
else:
    print("Aoki")

print(dp)
