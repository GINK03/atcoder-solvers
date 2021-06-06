
N,K=map(int,input().split())
S=[int(input()) for _ in range(N)]
if S.count(0) != 0:
    print(N)
    exit()

left,right=0,0

ans = 0
tmp = 1
diff = []
while left < N and right < N:
    if S[right]*tmp <= K:
        ans = max(ans, right-left+1)
        tmp *= S[right]
        right += 1
    else:
        if left == right:
            right += 1
        else:
            tmp /= S[left]
        left += 1
print(ans)
#print(diff)
