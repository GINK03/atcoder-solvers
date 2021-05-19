
import bisect
N = int(input())
A = list(map(int, input().split())) 
A.sort()
ans = 0
for i in range(2,N):#iは一番長い辺
    for j in range(1,i):#jは二番目に長い辺
        d = max(0, j-bisect.bisect_right(A, A[i]-A[j]) )
        ans += d
print(ans)
