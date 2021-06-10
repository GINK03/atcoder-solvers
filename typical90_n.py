
N=int(input())
*A,=map(int,input().split())
*B,=map(int,input().split())
A.sort()
B.sort()

print(sum(abs(a-b) for a,b in zip(A,B)))
