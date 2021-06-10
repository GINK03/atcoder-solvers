
N=int(input())

A = []
for _ in range(N):
    x,l=map(int,input().split())
    s = x - l
    t = x + l
    A.append( (s, t) )
A.sort(key=lambda x:x[1])

cur = -float("inf")
cnt = 0
for s, t in A:
    if cur <= s:
        cur = t
        cnt += 1

print(cnt)
