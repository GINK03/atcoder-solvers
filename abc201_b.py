N=int(input())

A=[]
for _ in range(N):
    S,T=input().split()
    T=int(T)
    A.append((T,S))
A.sort()

print(A[-2][1])

