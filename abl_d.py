


MAX = 3*(10**5)
A = [0] * MAX

N,K=map(int,input().split())
for n in range(N):
    a = int(input())-1
    A[min(MAX, a+K)] -= 1
    A[max(0, a-K-1)] += 1

import itertools

cumsum = [e for i, e in enumerate(list(itertools.accumulate(A)))]
print(cumsum[:100])
print(max(cumsum))

