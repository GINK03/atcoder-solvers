
import functools, math
N=int(input())
*A,=map(int,input().split())
print(functools.reduce(math.gcd, A))
