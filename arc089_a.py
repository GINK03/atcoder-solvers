
N=int(input())

pt, px, py = 0, 0, 0
def func():
    global pt, px, py
    t,x,y=map(int,input().split())
    if abs(x-px) + abs(y-py) <= t-pt and abs(x+y)%2 == t%2:
        pt, px, py = t, x, y
        return True
    else:
        pt, px, py = t, x, y
        return False
if all(func() for _ in range(N)):
    print("Yes")
else:
    print("No")
