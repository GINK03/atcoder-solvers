N,M=map(int,input().split())

X=[]
for _ in range(N):
    X.append(list(map(int,input().split())))

ans = 0
for i in range(M):
    for j in range(i+1,M):
        tmp = 0
        for k in range(N):
            tmp += max(X[k][i],X[k][j])
        #print(i,j, tmp)
        ans = max(ans, tmp)
print(ans)
         
