
N=int(input())
*A,=map(int,input().split())
A.sort()

Q=int(input())
B=[int(input()) for _ in range(Q)]

import bisect

ans = 0
for b in B:
    idx0 = min(N-1, max(0, bisect.bisect_left(A,b)-1))
    idx1 = min(N-1, max(0, bisect.bisect_left(A,b)))
    idx2 = min(N-1, bisect.bisect_right(A,b))
    ans = min(abs(A[idx0]-b), abs(A[idx1]-b), abs(A[idx2]-b)) 
    print(ans)

