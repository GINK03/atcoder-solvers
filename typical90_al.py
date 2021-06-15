import copy
from decimal import Decimal
A,B=map(Decimal, input().split())
Ad, Bd = copy.copy(A), copy.copy(B)

while B:
    A, B = B, A%B

if 10**18 < Ad//A*Bd:
    print("Large")
else:
    print(Ad//A*Bd)
