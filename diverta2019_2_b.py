import collections
N = int(input())

XY = []
for i in range(N):
    x, y = map(int,input().split())
    XY.append( (x, y) )

XY.sort()
cnt = collections.defaultdict(int)
for i in range(N-1):
    for j in range(i+1, N):
        (x0, y0), (x1, y1) = XY[i], XY[j]
        cnt[(x0 - x1, y0 - y1)] += 1

if len(cnt) != 0:
    (dx, dy), num = max(cnt.items(), key=lambda x:x[1])
    #print( dx, dy, num)
    print(N - num)
else:
    print(N)
