V,S,T,D=map(int,input().split())

sec = D/V
if S <= sec <= T:
    print("No")
else:
    print("Yes")
