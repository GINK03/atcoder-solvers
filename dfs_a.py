import collections
H,W=map(int,input().split())

G=[]
st = []
for h in range(H):
    arr = list(input())
    G.append(arr)
    for w in range(W):
        if arr[w] == 's':
            st = [h,w]
            break

que = collections.deque([st])


while que:
    h,w = que.pop()
    for dh,dw in [(1,0),(-1,0), (0,1), (0,-1)]:
        new_h=h+dh
        new_w=w+dw
        if new_h < 0 or new_w < 0 or new_h >= H or new_w >= W:
            continue
        st = G[new_h][new_w]
        if st == "#" or st == '/':
            continue
        if st == 'g':
            print("Yes")
            exit()
        que.append((new_h, new_w))
    G[h][w]='/'

#print(G)
print("No")


