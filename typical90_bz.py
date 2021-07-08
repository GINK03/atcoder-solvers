import collections

N,M=map(int,input().split())

p = collections.defaultdict(list)
for m in range(M):
    a,b=map(int,input().split())
    if a > b:
        p[a].append(b)
    if b > a:
        p[b].append(a)

cnt = 0
for edge, node in p.items():
    if len(node) == 1:
        cnt += 1

print(cnt)

