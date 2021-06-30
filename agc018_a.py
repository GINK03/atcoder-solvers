

import numpy as np
N,K=map(int,input().split())
*A,=map(int,input().split())

g = np.gcd.reduce(A)
if max(A) >= K:
    if K%g == 0:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")
