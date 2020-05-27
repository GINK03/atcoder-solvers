n,k=map(int,input().split())

if k > (n-1)*(n-2)//2:
    print(-1)
    exit()


max_num = (n-1)*(n-2)//2
st = [(1,t) for t in range(2, n+1)]

descrese_num = max_num - k
print(n -1 + descrese_num)
for s, t in st:
    print(s,t)

ps = [t for s,t in st]
from itertools import combinations
for idx, (p1,p2) in enumerate(combinations(ps,2)):
    print(p1, p2)
    if idx+1 >= descrese_num:
        break


