import os
N = int(input())
A = list(map(int,input().split()))

cnt = 0
right = 0
left = 0
while left < N:
    right = left + 1
    while right < N:
        if A[right-1] < A[right]:
            right += 1
        else:
            break
    cnt += (right-left)*(right-left-1)//2
    left = right

print(cnt+N)
