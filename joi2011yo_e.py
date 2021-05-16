import collections
H,W,N=map(int, input().split())

G=[]
for h in range(H):
    arr=list(input())
    G.append(arr)

points = []
for h in range(H):
    for w in range(W):
        if G[h][w] == 'S':
            points.append( (0, h, w) )
        elif G[h][w] in set("123456789"):
            points.append( (int(G[h][w]), h, w) )

points.sort()

acc = 0
while len(points) > 1:
    point, sh, sw = points.pop(0)

    visited = set()
    que = collections.deque([(sh,sw,0)])
    while que:
        h,w,cnt = que.popleft()
        if (h,w) in visited:
            continue
        visited.add((h,w))
        if G[h][w] == str(point+1):
            acc += cnt
            break
        for dh,dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nh=h+dh
            nw=w+dw
            if nh > H-1 or nh < 0 or nw < 0 or nw > W-1:
                continue
            if G[nh][nw] == "X":
                continue
            que.append( (nh,nw,cnt+1) )
    #print("de", point, cnt) 
print(acc)
