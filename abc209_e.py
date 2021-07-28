
import collections
N = int(input())
keys = set()
G = collections.defaultdict(list)
cnt = collections.defaultdict(int)
S = []
for i in range(N):
    s = input()
    S.append(s)
    h, t = s[:3], s[-3:]
    keys.add( h )
    keys.add( t )
kp ={ key:i for i, key in enumerate(keys)}
for s in S:
    h, t = s[:3], s[-3:]
    i, j = kp[h], kp[t]
    G[j].append(i)
    cnt[kp[h]] += 1

""" 自分で考えたアプローチ """
# wfで最短を計算
# ぐう気であれをgrundyを計算

""" 正解 """
# 後退解析と呼ばれるアルゴリズムを用いることで解くことができます。

ans = [-1]*len(kp)
que = collections.deque([])
for i in range(len(kp)):
    if cnt[i] == 0:
        que.append(i)
        ans[i] = 0

while que:
    i = que.popleft()
    for j in G[i]:
        if ans[j] == -1:
            cnt[j] -= 1
            if ans[i] == 0:
                ans[j] = 1
                que.append(j)
            elif cnt[j] == 0:
                ans[j] = 0
                que.append(j)
for s in S:
    h, t = s[:3], s[-3:]
    if ans[kp[t]] == -1:
        print("Draw")
    elif ans[kp[t]] == 0:
        print("Takahashi")
    else:
        print("Aoki")
