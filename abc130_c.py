W,H,x,y=map(int,input().split())

print(W*H/2,1 if x*2==W and y*2==H else 0)
