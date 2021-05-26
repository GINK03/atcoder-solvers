

import collections
N=int(input())
D=list(map(int,input().split()))
D=dict(collections.Counter(D))
M=int(input())
T=list(map(int,input().split()))

for t in T:
    if t in D:
        if D[t] == 0:
            print("NO")
            exit()
        D[t] -= 1
    else:
        print("NO")
        exit()
print("YES")

