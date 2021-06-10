
import sys; sys.setrecursionlimit(10**9)
import collections

N=int(input())
G=[[] for _ in range(N)]

for _ in range(N-1):
    a,b=map(int,input().split())
    a-=1;b-=1
    G[a].append(b)
    G[b].append(a)

nt = [None]*N
que = collections.deque([(0,0)])
while que:
    i, arg = que.pop()
    nt[i] = arg
    for j in G[i]:
        if nt[j] is None:
            que.append((j, 1^arg))


dic = collections.Counter(nt)
flg, num = max(dic.items(), key=lambda x:x[1])

max_n = N//2
cnt = 0
for i, n in enumerate(nt,1):
    if n == flg:
        print(i, end=" ")
        cnt += 1
        if cnt >= max_n:
            break
print()
