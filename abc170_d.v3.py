
N = int(input())
*A,=map(int,input().split())
max_a = max(A)

dp = [0] * (max_a+1)

for a in A:
    tmp = a
    cnt = 1
    while True:
        dp[tmp] += 1
        cnt += 1
        tmp = a * cnt
        if tmp > max_a:
            break

ans = 0
for a in A:
    ans += 1 if dp[a] == 1 else 0
print(ans)

