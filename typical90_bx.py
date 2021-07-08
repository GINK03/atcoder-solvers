import itertools
import bisect
N = int(input())
*A,=map(int,input().split())

if sum(A)%10 != 0:
    print("No")
    exit()

T = sum(A)//10
*B,=itertools.accumulate(A+A)

for i in range(N):
    goal = B[i] + T
    idx = bisect.bisect_left(B, goal)
    if B[idx] == goal:
        print("Yes")
        exit()

print("No")
