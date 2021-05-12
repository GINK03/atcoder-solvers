N=int(input())

L=[]
for i in range(N):
    A,B=map(int,input().split())
    L.append( (i, A,B,A+B))


L.sort(key=lambda x:x[1])
i0, a0, b0, ab0 = L[0]
for i in range(len(L)):
    L.sort(key=lambda x:x[2])
    if L[i][0] != i0:
        break
i0_, a0_, b0_, ab0_ = L[i]

t0 = max(a0,b0_)


# p2
L.sort(key=lambda x:x[2])
i1, a1, b1, ab1 = L[0]
for i in range(len(L)):
    L.sort(key=lambda x:x[1])
    if L[i][0] != i1:
        break
i1, a1_, b1_, ab1_ = L[i]
t1 = max(b1,a1_)


# 同じ人
L.sort(key=lambda x:x[3])
i2, a2, b2, ab2 = L[0]
print(min([ab2, t0, t1]))

