import collections
H,W=map(int,input().split())
sh,sw=map(int,input().split())
sh-=1;sw-=1
gh,gw=map(int,input().split())
gh-=1;gw-=1

G=[]
for h in range(H):
    arr=list(input())
    G.append(arr)


que = collections.deque([ [sh,sw, 0] ])

while que:
    h,w, cnt = que.popleft()
    if G[h][w] != '.':
        continue
    G[h][w] = cnt
    if (h,w) == (gh,gw):
        print(cnt) 

    for dh,dw in [(1,0), (-1,0), (0,1), (0,-1)]:
        nh=h+dh
        nw=w+dw
        if nh <0 or nw<0 or nh>=H or nw>=W or G[nh][nw] != '.':
            continue
        que.append([nh,nw,cnt+1])

