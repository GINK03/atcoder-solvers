import sys; sys.setrecursionlimit(10**9)
import collections
N = int(input())
K = int(input())
G = [list(input()) for i in range(N)]

ans = 0
vis = collections.defaultdict(lambda :False)
done = set()
def dfs(h, w, v, prev):
    global ans
    vis[(h, w)] = True

    idx = N*h + w
    v += 1 << idx
    if v in done:
        return
    done.add(v)

    if len(prev) == K:
        ans += 1
        return 
    for ph, pw in prev:
        for dh, dw in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nh, nw = ph+dh, pw+dw
            if 0 <= nh < N and 0 <= nw < N and G[nh][nw] == '.' and not vis[(nh, nw)]:
                prev.append((nh, nw))
                dfs(nh, nw, v, prev)
                prev.pop()
                vis[(nh, nw)] = False

for h in range(N):
    for w in range(N):
        if 0 <= h < N and 0 <= w < N and G[h][w] == '.':
            vis = collections.defaultdict(lambda :False)
            dfs(h, w, 0, [(h, w)])

print(ans)
    
