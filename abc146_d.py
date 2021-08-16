import collections
import sys
input = sys.stdin.readline

N = int(input())

G = collections.defaultdict(collections.deque)
for n in range(N-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append( (b, n) )
    G[b].append( (a, n) )

K = max([len(v) for v in G.values()])


def bfs():
    que = collections.deque([0])
    bans = collections.defaultdict(set) # vの使用済みの色を保存する
    edge_color = [0]*(N-1) # eの可能性のある最小の色を保存する
    vtd = set()
    while que:
        i = que.popleft()
        if i in vtd:
            continue
        vtd.add(i)
        colors = iter(c for c in range(K) if c not in bans[i]) # iterにしないとめちゃ重い
        for j, edge in G[i]:
            if j in vtd:
                continue
            que.append(j)
            color = next(colors)
            edge_color[edge] = color + 1
            bans[i].add(color)
            bans[j].add(color)
    return edge_color

edge_color = bfs()
print(K)
print(*edge_color, sep="\n")


