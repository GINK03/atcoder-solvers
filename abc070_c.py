import math
N=int(input())

A = [int(input()) for _ in range(N)]

lcm = 1
for a in A:
    lcm = lcm*a//math.gcd(lcm, a)

print(lcm)
