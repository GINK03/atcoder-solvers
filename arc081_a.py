import collections
N=int(input())
*A,=map(int,input().split())
kv = [(k,v//2) for k,v in collections.Counter(A).items()]
kv.sort()
*kv,=filter(lambda x:x[1] > 0, kv)


for i in range(len(kv)-1, -1, -1):
    if kv[i][1] >= 2:
        print(kv[i][0]**2)
        exit()
    else:
        if i-1 >= 0:
            print(kv[i][0]*kv[i-1][0])
            exit()
print(0)
