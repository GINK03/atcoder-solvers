a,b=input().split()

from decimal import *
getcontext().prec = 100
a=Decimal(a)
b=Decimal(b)
print(int(a*b))


