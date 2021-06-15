
import collections
N,K=map(int,input().split())
*A,=map(int,input().split())

left, right = 0, 0
wa, ans = 0, 0

while left < N:
    while right < N:
        if wa + A[right] >= K:
            break
        wa += A[right]
        right += 1 # インクリメントは最後
    ans += right - left 
    wa -= A[left]
    left += 1
    if right == left:
        right = left

print(N*(N+1)//2 -ans)
