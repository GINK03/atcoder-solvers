import math
import statistics

H,W=map(int,input().split())

G=[]
for h in range(H):
    G.append( list(input()) )

a=0
for h in range(1,H):
    for w in range(1,W):
        tmp = 0
        for fh, fw in [(-1, -1), (-1, 0), (0, -1), (0, 0)]:
            new_h = h + fh
            new_w = w + fw
            if G[new_h][new_w] == "#":
                tmp += 1
        if tmp in {1, 3}:
            a += 1
print(a)
