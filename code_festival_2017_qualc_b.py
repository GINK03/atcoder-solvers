import numpy as np
N=int(input())
A=list(map(int,input().split()))

pt = [sum([(a+p)%2==1 for p in [-1, 0, 1]]) for a in A]
print(3**N - np.prod(pt))

