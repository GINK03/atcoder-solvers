
N,X=map(int,input().split())
A=list(map(int,input().split()))
import numpy as np
print(np.gcd.reduce(np.abs(np.array(A)-X)))


