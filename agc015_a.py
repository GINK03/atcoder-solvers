

N,A,B=map(int,input().split())

if (N == 1 and A != B) or (B-A > N):
    print(0)
    exit()
ans = max(0, (B-A)*(N-2) +1)
print(ans)

