
import math

N,M=map(int,input().split())
A=list(map(int,input().split()))
A=list(map(lambda x:x%2, A))


x0 = A.count(0)
x1 = A.count(1)

if x0 == N and M==0:
    print(2**x0)
    exit()
if x0 == N:
    print(0)
    exit()
print(2**(N-1))


