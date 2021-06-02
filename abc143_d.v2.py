
import bisect
import itertools
N = int(input())
*A, = map(int, input().split())
A.sort()
*AI,=range(N)
   

acc = 0
for j, i in itertools.combinations(AI,2):
    # j < i 
    # a < b + cより a - b < cならばよい
    num = j - bisect.bisect_right(A, A[i] - A[j])
    if num > 0:
        acc += num
print(acc)
