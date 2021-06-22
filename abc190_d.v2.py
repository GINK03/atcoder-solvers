import math

N = int(input())

while True:
    if N%2 == 0:
        N //= 2
    else:
        break


cnt = 0
for d in range(1, int(N**0.5)+1):
    if N%d == 0:
        cnt += 2

if int(N**0.5) ** 2 == N:
    cnt -= 1

print(cnt*2)
        
