
N = int(input())

XYH = []
for n in range(N):
    x,y,h = map(int, input().split())
    XYH.append( (x,y,h) )
XYH.sort(key=lambda x: x[2], reverse=True)

CANS = []
for sx in range(100+1):
    for sy in range(100+1):
        x, y, h = XYH[0]
        ch = h + abs(x - sx) + abs(y - sy)
        ng = False
        for x, y, h in XYH:
            if h != max(ch - abs(sx - x) - abs(sy - y), 0):
                ng = True
        if ng == False:
            CANS.append( (sx, sy, ch) )


for sx, sy, ch in CANS:
    for x, y, h in XYH:
        if h == max(ch - abs(sx - x) - abs(sy - y), 0):
            print(sx, sy, ch); exit()
        
    
