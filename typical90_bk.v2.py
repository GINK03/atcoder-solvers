import collections

H, W = map(int, input().split())

G = [[0] * W for _ in range(H)]

for h in range(H):
    *ln, = map(int, input().split())
    for w in range(W):
        G[h][w] = ln[w]


ans = 0
for i in range(1 << H):
    ints = collections.defaultdict(int)
    
    for w in range(W):
        tmp = None
        ok = True
        for j in range(H):
            if i&(1<<j) == 0:
                continue
            if tmp is None:
                tmp = G[j][w]
            elif tmp != G[j][w]:
                ok = False
                break
        if ok:
            ints[tmp] += 1
    if len(ints) == 0:
        continue
    # intsの中から最大の数を取り出す
    max_int = max(ints.values())
    # iのbitの1の数
    h_num = format(i, "b").count("1")
    ans = max(ans, h_num*max_int)
print(ans)

