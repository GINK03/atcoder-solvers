
N,K,S=map(int,input().split())

if S == 10**9:
    B = [S]*K + [1]*(N-K)
else:
    B = [S]*K + [S+1]*(N-K)
print(" ".join(map(str,B)))
