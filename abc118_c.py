
import numpy as np
N=int(input())
*A,=map(int,input().split())
print(np.gcd.reduce(A))
