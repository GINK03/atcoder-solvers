
import math
A,B,C=map(int,input().split())

a = A
for x in [B,C]:
    a = math.gcd(a, x)

A,B,C=map(lambda x:x//a-1, [A,B,C])
print(sum([A,B,C]))




