import numpy as np
import itertools

N=int(input())
A=np.array([list(map(int,input().split())) for _ in range(N)])

cnt = 0
acc = 0
for i in itertools.permutations(range(0,N)):
    cnt += 1
    tmp = A[list(i)]
    for k in range(0, N-1):
        # acc += ((tmp[k]-tmp[k+1])**2).sum()**0.5
        acc += np.linalg.norm(tmp[k]-tmp[k+1])

print(acc/cnt)
