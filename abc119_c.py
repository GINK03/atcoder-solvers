import collections
N,A,B,C=map(int,input().split())
L = [int(input()) for i in range(N)]

Elm = collections.namedtuple("elm", ["depth", "a", "b", "c", "point"])

ans = float('inf')

que = collections.deque([Elm(0, 0, 0, 0, 0)])
while que:
    depth, a, b, c, point = que.pop()
    
    if min(a, b, c) > 0 and depth == N:
        ans = min(ans, abs(a-A)+abs(b-B)+abs(c-C)-30+point)
    if depth >= N:
        continue
    que.append( Elm(depth+1, a, b, c, point) )
    que.append( Elm(depth+1, a+L[depth], b, c, point+10) )
    que.append( Elm(depth+1, a, b+L[depth], c, point+10) )
    que.append( Elm(depth+1, a, b, c+L[depth], point+10) )
print(ans)
