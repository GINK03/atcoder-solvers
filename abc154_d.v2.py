import itertools
N, K = map(int, input().split())
A = list(map(int, input().split()))

# サイコロは独立なのですべてを独立に期待値を計算する
B = []
for a in A:
    b = (1 / a) * (1 / 2 * a * (a + 1))
    B.append(b)

if N == K:
    ans = sum(B)
else:
    ans = 0

ACC = list(itertools.accumulate(B))

# 累積和から差分を取ることで計算
for i in range(0, len(ACC) - K):
    ans = max(ans, ACC[i + K] - ACC[i])

print(ans)
