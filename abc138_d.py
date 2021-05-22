import collections

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

X = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1
    X[p] += x

parent = [-1] * N
que = collections.deque([0])
while que:
    now = que.pop()
    for to in G[now]:
        if to == parent[now]:
            continue
        X[to] += X[now]
        que.append(to)
        parent[to] = now
print(*X)
