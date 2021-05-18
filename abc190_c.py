N,M=map(int,input().split())
AB=[]
for _ in range(M):
    AB.append(list(map(int,input().split())))
K=int(input())
P=1<<K
CD=[]
for _ in range(K):
    CD.append(list(map(int,input().split())))


max_ = 0
for i in range(P):
    tmp = [0]*(N+1)
    for j in range(K):
        if i&(1<<j) > 0:
            tmp[CD[j][0]]=1
        else:
            tmp[CD[j][1]]=1
    cnt = 0
    for a,b in AB:
        if tmp[a] and tmp[b]:
            cnt += 1
    max_ = max(cnt, max_)
print(max_)

