
N,K=map(int,input().split())

for _ in range(K):
    if N%200 == 0:
        N //= 200
    else:
        tmp = str(N) + "200"
        N = int(tmp)
print(N)
