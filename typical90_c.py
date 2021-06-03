import collections

N = int(input())
G = collections.defaultdict(list)

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)


def bfs(que: collections.deque):
    vmem = collections.defaultdict(int)
    vd = set()
    while que:
        i, depth = que.popleft()
        if i in vd:
            continue
        vd.add(i)
        vmem[i] = depth
        for j in G[i]:
            que.append((j, depth + 1))
    return vmem


que = collections.deque([(0, 0)])
vmem = bfs(que)
v, k = max([(v, k) for k, v in vmem.items()])
que = collections.deque([(k, 0)])
vmem = bfs(que)
print(max(vmem.values()) + 1)
