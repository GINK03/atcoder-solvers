import collections

N=int(input())

dic = collections.defaultdict(int)
for _ in range(N):
    a,b=map(int,input().split())
    dic[a]+=1
    dic[b+1]-=1


A=[0]*1000001
A[0] = dic[0]

for i in range(1,1000001):
    f=0
    if i in dic:
        f = dic[i]
    A[i] = A[i-1]+f

print(max(A))
