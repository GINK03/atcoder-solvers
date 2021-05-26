
N=int(input())
A=list(map(int,input().split()))
import numpy as np
A=np.array(A)-1
print(sum([A[A[i]] == i for i in range(N)])//2)

