N,M=map(int,input().split())

xs = []
for n in range(N):
    A,B=map(int,input().split())
    xs.append( (A,B))

m = 0
c = 0
for a,b in sorted(xs,key=lambda x:x[0]):
    if m+b <= M:
        m+=b
        c+=a*b
    else:
        #print('b', M-m)
        c+=a*(M-m)
        m+=M-m
        break
print(c)

