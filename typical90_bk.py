import collections

H, W = map(int, input().split())

G = [[0] * W for _ in range(H)]

for h in range(H):
    *ln, = map(int, input().split())
    for w in range(W):
        G[h][w] = ln[w]


ans = 0
for i in range(1 << H):
    R = collections.defaultdict(int)
    # 横一覧を見ていく
    for w in range(W):
        tmp = None
        flag = False
        # 縦にスキャンしていく
        for k in range(H):
            if i & (1 << k) == 0:
                continue
            if tmp is None:
                tmp = G[k][w]
            elif tmp != G[k][w]:
                flag = True
        # あるjですべて同じ数で構成されていれば
        if flag == False:
            R[tmp] += 1
        
    cnt_h = format(i, "b").count('1')
    if len(R) > 0:
        cnt_w = max(R.values())
    else:
        continue
    # print(i, cnt_h, cnt_w)
    ans = max(cnt_h*cnt_w, ans)
print(ans)
