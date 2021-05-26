import itertools
import math
N,D=map(int,input().split())

X=[]
for _ in range(N):
    X.append(list(map(int,input().split())))


cnt = 0
for s0, t0 in itertools.combinations(X,2):
    tmp = [(a-b)**2 for a, b in zip(s0, t0)]
    tmp = sum(tmp) 
    if tmp == int(math.sqrt(tmp))**2:
        cnt += 1
print(cnt)
