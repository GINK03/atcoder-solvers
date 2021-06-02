import collections
import bisect
N,M=map(int,input().split())
*A,=map(int,input().split())


af = collections.defaultdict(int)
for a in A:
    af[a] += 1

BC = []
[BC.append(list(map(int, input().split()))) for _ in range(M)]

for b,c in BC:
    af[c] += b

# 上位 TOP Nを取る
n = 0
ans = 0
for a, f in sorted(af.items(), reverse=True):
    if N >= n + f:
        n += f
        ans += a * f
    else:
        nokori = N - n 
        ans += a * nokori
        break
print(ans)



