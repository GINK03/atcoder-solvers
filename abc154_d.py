import itertools
N, K = map(int, input().split())
A = list(map(int, input().split()))

B = []
for a in A:
    b = (1 / a) * (1 / 2 * a * (a + 1))
    B.append(b)
#print(B)
if N == K:
    ans = sum(B)
else:
    ans = 0
B = list(itertools.accumulate(B))
# print(B)
for i in range(len(B) - K):
    ans = max(ans, B[i + K] - B[i])

print(ans)
