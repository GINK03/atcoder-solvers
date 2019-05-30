
N,M,C=map(int,input().split())
Bs=[int(b) for b in input().split()]

c=0
for n in range(N):
    As=[int(a) for a in input().split()]
    r = sum([a*b for a,b in zip(As,Bs)]) + C
    if r>0:
        c+=1
    #print(r)
print(c) 
