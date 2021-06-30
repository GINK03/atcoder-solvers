import collections

N = int(input())
G = [[] for _ in range(N)]

for n in range(N):
    x = int(input())
    x -= 1
    G[n].append(x)


vis = set()
ans = 0

def trys(start):
    global ans
    if start in vis:
        return
    cnts = [-1]*N
    def dfs(i, cnt):
        if i in vis:
            return
        vis.add(i)
        cnts[i] = cnt
        for j in G[i]:
            dfs(j, cnt+1)
    dfs(start, 0) 
    ms = [c%2 for c in cnts if c >= 0]
    tmp = 0
    for v in collections.Counter(ms).values():
        if v == 1:
            print(-1); exit()
        tmp += v
    ans += tmp//2

[trys(i) for i in range(N)]
print(ans)

