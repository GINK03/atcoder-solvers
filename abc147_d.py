
MOD = 10**9 + 7
N = int(input())
*A, = map(int, input().split())

L = [[0, 0] for i in range(60)]

for a in A:
    for i, b in enumerate(format(a, "060b")[::-1]):
        b = int(b)
        L[i][b] += 1

ans = 0
for i, (num0, num1) in enumerate(L):
    ans += pow(2, i, MOD) * num1 * num0
    ans %= MOD
print(ans)

