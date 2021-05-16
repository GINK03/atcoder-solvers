import math
N,G=map(int,input().split())

A=[]
for i in range(1,N+1):
    score = i*100
    num,comp=map(int,input().split())
    A.append((score, num, comp))

P = 1<<len(A)

ans = math.inf
for i in range(P):
    num = 0
    score = 0
    for j in range(len(A)):
        if i&(1<<j) > 0:
            score += A[j][2] + A[j][0]*A[j][1]
            num += A[j][1]
    
    if G > score:
        for j in reversed(range(len(A))):
            if i&(1<<j) == 0:
                for _ in range(A[j][1]):
                    score += A[j][0]
                    num += 1
                    if G <= score:
                        break
                if G <= score:
                    break
    
    ans = min(ans, num)
print(ans)
