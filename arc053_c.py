
N = int(input())

AB = [list(map(int,input().split())) for _ in range(N)]

'''温度を結果的に下げるグループをL
温度を結果的に上げるグループをR
'''
L = [(a, b) for a, b in AB if a < b]
R = [(a, b) for a, b in AB if a >= b]

'''greedy的に考えると、Lはaが小さいものから入れていけば良い
Rはbが大きいものから入れていけば良い
Lが最初でRが次
'''
L.sort()
R.sort(key=lambda x:-x[1])

ans = 0
tmp = 0
for a, b in L:
    tmp += a
    ans = max(ans, tmp)
    tmp -= b

for a, b in R:
    tmp += a
    ans = max(ans, tmp)
    tmp -= b

print(ans)
