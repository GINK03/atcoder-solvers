x,y=map(int,input().split())

can = float("inf")
if y - x >= 0:
    can = min(can, y - x)
if -y - x >= 0:
    can = min(can, -y - x + 1)
 
if y - (-x) >= 0:
    can = min(can, y + x + 1)
if -y - (-x) >= 0:
    can = min(can, -y + x + 2)

print(can)

