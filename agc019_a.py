
#1Lあたりの値段を求める
A,B,C,D=map(int,input().split())
A*=4
B*=2
A=min(A,B,C)
N=int(input())
if 2*A <= D:
  print(N*A)
else:
  print((N//2)*D + (N%2)*A)


