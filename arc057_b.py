N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

if sum(A) == K:
    exit(print(1))

DP = [float('inf')] * (N + 1) #これまでにn日期限が良かった時の勝数の最小値
DP[0] = 0
DP[1] = 1
done = A[0]
for i, a in enumerate(A[1:], 1):
    D = DP[:]
    for j in range(i + 1):
        x = D[j] + D[j] * a // done 
        while x * done <= D[j] * (done + a): # ギリギリの勝率
            x += 1
        DP[j + 1] = min(DP[j + 1], x)
    done += a
 
 
ans = 0
for i, dp in enumerate(DP):
    if dp <= K:
        ans = max(ans, i)
print(ans)
