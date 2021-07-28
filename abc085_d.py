import math
N, H = map(int,input().split())

AB = []
for n in range(N):
    a,b = map(int,input().split())
    AB.append( (a, b) )
AB.sort(key=lambda x:x[0])

max_a, _b = AB[-1]
use_b = [b for a, b in AB if b > max_a]
b_size = len(use_b)


cnt = 0
use_b.sort()
n_diff = H
for i in range(b_size)[::-1]:
    n_diff -= use_b[i]
    cnt += 1
    if n_diff <= 0:
        print(cnt)
        exit()

if n_diff > 0:
    a_num = math.ceil(n_diff / max_a)
    print(a_num + cnt)
else:
    print(cnt)
