
N, K = map(int, input().split())
ans = 0
count = 0
sub = 0
 
for i in range(1, N+1):
    count = 0
    ans = 1/N
    while i < K:
        i *= 2
        ans *= 0.5
        count += 1
    sub += ans
print(sub)
