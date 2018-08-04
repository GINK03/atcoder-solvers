
''' このソリューションはおもすぎる 
from fractions import gcd
from functools import reduce
def lcm(a,b): return abs(a * b)/gcd(a,b) if a and b else 0

n = input()
xs = [int(x) for x in input().split()]

mlcm = 1
for x in set(xs):
  mlcm = lcm(mlcm, x)

mlcm -= 1
mlcm = int(mlcm)
print(sum([ mlcm%x for x in xs]))
'''

n = input()
xs = [int(x)-1 for x in input().split()]
print(sum(xs))
