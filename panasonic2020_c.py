
from decimal import Decimal
a,b,c=map(Decimal,input().split())

if (a+b-c)**2 > 4*a*b and c-a-b > 0:
    print("Yes")
else:
    print("No")
