
import collections
import copy

G=[]
NUM=0
for i in range(10):
    lst = list(input())
    for chr in lst:
        if chr == 'o':
            NUM += 1
    G.append(lst)


def dfs(que):
    mem = set()
    cnt = 0
    while que:
        h,w = que.pop()
        if (h,w) in mem:
            continue
        mem.add((h,w))

        if G[h][w] == 'o':
            cnt += 1
        for dh,dw in [(1,0), (-1,0), (0,-1), (0,+1)]:
            nh=h+dh
            nw=w+dw
            if nh < 0 or nw < 0 or 10 <= nh or 10 <= nw:
                continue
            if G[nh][nw] == 'x':
                continue
            que.append((nh,nw))    
    return cnt

for i in range(10):
    for j in range(10):
        start = (i,j)
        que = collections.deque([(i,j)])
        cnt = dfs(que)
        #print(i,j,cnt, NUM)
        if cnt == NUM:
            print("YES")
            exit()
print("NO")

