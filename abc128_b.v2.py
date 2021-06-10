
N=int(input())

A = []
for i in range(N):
    s,p=input().split()
    p = int(p)
    A.append( (s,-p, i+1) )
A.sort()
for s, np, i in A:
    print(i)
