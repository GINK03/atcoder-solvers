K,S=map(int,input().split())

cnt =0
for x in range(K+1):
    for y in range(K+1):
        z=S-x-y
        if K>=z>=0:
            cnt+=1
print(cnt)

