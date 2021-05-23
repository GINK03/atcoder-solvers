import numpy as np
N=int(input())
X=np.array(list(map(int,input().split())))
a =min( ((X-np.ceil(X.mean()))**2).sum(), ((X-np.floor(X.mean()))**2).sum() )
print(int(a))

