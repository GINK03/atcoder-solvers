import collections
import copy
H,W=map(int,input().split())
G=[]
for h in range(H):
    G.append(list(input()))

G[0][0]='.'

que = collections.deque([ [0,0,'T', G] ] )
min_ans = []
points = {'T':0, 'A':0}

while que:
    x, y, user, G = que.popleft() 
    is_flag = False
    tmp = []
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_x = x+dx
        new_y = y+dy

        if new_x < 0 or new_x >= H or new_y < 0 or new_y >= W:
            continue
        if G[new_x][new_y] == '+':
            tmp.append((1, new_x, new_y))
        elif G[new_x][new_y] == '-':
            tmp.append((-1, new_x, new_y))
        else:
            continue

    tmp.sort()
    if tmp == []:
        continue
    
    p, new_x, new_y = tmp[-1] 
    points[user] += p
    if user == 'T':
        new_user = 'A'
    else:
        new_user = 'T'
    #nG=copy.deepcopy(G)
    G[new_x][new_y] = '.'
    que.append([new_x, new_y, new_user, G])



if points['T'] > points['A']:
    print("Takahashi")
elif points['T'] < points['A']:
    print("Aoki")
else:
    print("Draw")

#print(points)
