import collections

H,W,X,Y=map(int,input().split())
X-=1
Y-=1

G=[]
for h in range(H):
    G.append(list(input()))
     

def dfs(G):
    while que:
        cur = que.pop()
        if cur in visited:
            continue
        visited.add(cur)
        for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_h = cur[0] + move[0]
            new_w = cur[1] + move[1]
            if new_h < 0 or new_h >= H or new_w < 0 or new_w >= W:
                continue
            # XかYのどちらかは少なくとも同じでなくては矛盾する
            if not(new_h == X or new_w == Y):
                continue
            if G[new_h][new_w] == "#":
                continue
            que.append((new_h, new_w))
    return visited

que = collections.deque([(X, Y)])
visited = set()
print(len(dfs(G)))
