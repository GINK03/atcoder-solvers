
N,M,K=map(int,input().split())

# 縦の操作と横の操作は独立であるから
# K = m*(M - n) + n*(N-m)

for m in range(M+1):
    for n in range(N+1):
        if K == n*(M - m) + m*(N-n):
            print("Yes")
            exit()
print("No")
