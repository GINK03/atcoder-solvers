

import numpy as np
N,K=map(int,input().split())
*A,=map(int,input().split())

a = np.gcd.reduce(A)
if max(A) >= a:
    if K%a == 0:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")
