A,B=map(int,input().split())
A+=B
if A >= 15 and B >= 8:
    print(1)
elif A >= 10 and B >= 3:
    print(2)
elif A >= 3:
    print(3)
else:
    print(4)
