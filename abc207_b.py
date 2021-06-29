

A,B,C,D=map(int,input().split())

# (C*D - B)*n >= A
import math

if C*D - B == 0:
    print(-1)
    exit()
n = math.ceil( A/(C*D-B) )

if n >= 0:
    print(n)
else:
    print(-1)
