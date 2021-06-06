
N = int(input())
XY = []
for _ in range(N):
    x,y=map(int,input().split())
    XY.append( (x+y, x-y) ) 


def cals(XY):
    x0,y0 = XY[0]
    x0,y0 = (x0+y0)//2, (x0-y0)//2 

    x1,y1 = XY[-1]
    x1,y1 = (x1+y1)//2, (x1-y1)//2 

    ans0 = abs(x0-x1) + abs(y0-y1)
    return ans0

XY.sort(key=lambda x:x[0])
ans0 = cals(XY)
XY.sort(key=lambda x:x[1])
ans1 = cals(XY)
print(max(ans0, ans1))


