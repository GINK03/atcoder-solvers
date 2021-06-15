
import collections
N,Q=map(int,input().split())

A = []
E = collections.namedtuple("E", ["X", "Y", "x", "y"])

for _ in range(N):
    x,y=map(int,input().split())
    A.append(E(X=x+y, Y=y-x, x=x, y=y))

minX, minY = min(map(lambda x:x.X, A)), min(map(lambda x:x.Y, A))
maxX, maxY = max(map(lambda x:x.X, A)), max(map(lambda x:x.Y, A))

for q in range(Q):
    qi = int(input())-1
    qX, qY, qx, qy = A[qi]
    cans = [abs(qX-minX), abs(qX-maxX), abs(qY-minY), abs(qY-maxY)]
    print(max(cans))
