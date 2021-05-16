import itertools
import math

MAX=10**10
sq = int(MAX ** 0.5)
s = set()
for a in range(2, sq + 1):
    x = a * a
    while x <= MAX:
        s.add(x)
        x *= a

N = int(input())
t = [s0 for s0 in s if s0 <= N]
print(N - len(t))

