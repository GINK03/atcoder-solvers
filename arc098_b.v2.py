
N=int(input())
*A,=map(int,input().split())

import collections
left_max = collections.defaultdict(int)


ans = 0
left, right = 0, 0
acc0, acc1 = 0, 0
while left < N:
    while right < N:
        if acc0 + A[right] != acc1 ^ A[right]:
            break
        acc0 += A[right]
        acc1 ^= A[right]
        right += 1
    ans += right - left
    acc0 -= A[left]
    acc1 = A[left]^acc1
    if left > right:
        right = left
    left += 1
print(ans)
