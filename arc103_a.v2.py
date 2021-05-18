
N=int(input())
A=list(map(int,input().split()))

lst0, lst1 = [], []

for i in range(N):
    if i%2 == 0:
        lst0.append(A[i])
    else:
        lst1.append(A[i])

import collections

vk0 = [(v,k) for k,v in collections.Counter(lst0).items()]
vk1 = [(v,k) for k,v in collections.Counter(lst1).items()]

vk0.sort()
vk1.sort()

v00, k00 = vk0[-1]
v01 = vk0[-2][0] if len(vk0) >= 2 else 0
v10, k10 = vk1[-1]
v11 = vk1[-2][0] if len(vk1) >= 2 else 0

if k00 != k10:
    print(N//2-v00+N//2-v10)
else:
    print(min(N - v01 - v10, N - v00 - v11))
