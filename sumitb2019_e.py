
N = int(input())
*A, = map(int, input().split())
MOD = 10**9 + 7
ans = 1

s = [0, 0, 0]
for n in range(N):
    ans *= s.count(A[n])
    if ans == 0:
        break
    ans %= MOD
    s[s.index(A[n])] += 1
print(ans)

