# import bisect
N = int(input())
A = list(map(int, input().split()))

ans = 1
flag = 0
now = A[0]
for i in A[1:]:
    if flag == 0 and now > i:
        flag = -1
    elif flag == 0 and now < i:
        flag = 1
    elif flag == -1 and now < i:
        ans += 1
        flag = 0
    elif flag == 1 and now > i:
        ans += 1
        flag = 0
    now = i
print(ans)
