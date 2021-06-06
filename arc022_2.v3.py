N=int(input())
*A,=map(int,input().split())


ans = 0
left, right = 0, 0
tmp = set()
while left < N and right < N:
    if A[right] not in tmp:
        tmp.add(A[right])
        right += 1
        ans = max(len(tmp), ans)
    else:
        tmp.remove(A[left])
        left += 1
        if left > right:
            right = left

print(ans)
