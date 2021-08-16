import collections

N, M =map(int, input().split())

cnt = collections.defaultdict(int)
for m in range(M):
    a, b = map(int, input().split())
    cnt[a] += 1
    cnt[b] += 1

flg = True
for v in cnt.values():
    if v%2 != 0:
        flg = False
if flg:
    print("YES")
else:
    print("NO")


