import math
N=int(input())

a = math.ceil(N/1.08)
b = math.floor(N/1.08)

buff = -1
for c in [b,a,b+1,a+1]:
    if math.floor(c*1.08) == N:
        buff = c

if buff != -1:
    print(buff)
else:
    print(":(")
