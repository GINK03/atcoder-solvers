
N = int(input())

XY = []
for n in range(N):
    x, y = map(int, input().split())
    XY.append( (x,y) )
XY.sort()
t = set(XY)
import itertools


ans = 0
for (x0, y0), (x1, y1) in itertools.combinations(XY, 2):
    if x0 < x1 and y0 < y1:
        if (x0, y1) in t and (x1, y0) in t:
            ans += 1
print(ans)

