import numpy as np

R, C = map(int, input().split())
G = np.array([list(map(int, input().split())) for _ in range(R)])
P = 1 << R
ans = 0
for i in range(P):
    g = G.copy()
    for j in range(R):
        if i & (1 << j) > 0:
            g[j] *= -1
            g[j] += 1
    s = g.sum(axis=0)
    ans = max(ans, np.maximum(R-s,s).sum())
print(ans)
