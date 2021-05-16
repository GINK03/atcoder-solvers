import collections

N, M = map(int, input().split())

G = collections.defaultdict(set)

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].add(v)
    G[v].add(u)

ans = 0
vis = [0] * N
for i in range(N):
    # 探索済みでないノードを見つけて初期値にセット
    if vis[i] != 0:
        continue
    has_loop = False
    que = collections.deque([i])

    while que:
        i = que.pop()
        vis[i] += 1
        # 参照が2箇所以上からされるならばそれはループしている(閉路が構築されている)
        if vis[i] >= 2:
            has_loop = True
            continue
        for ni in G[i]:
            # もとに戻るノードが存在する場合,カットする
            if i in G[ni]:
                G[ni].remove(i)
            que.append(ni)
    if has_loop == False:
        ans += 1
print(ans)
