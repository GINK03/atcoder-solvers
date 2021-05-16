
import decimal
import math

X,Y,R = list(map(decimal.Decimal, input().split()))
maxX = math.floor(X+R)
minX = math.ceil(X-R)

ans = 0
for x in range(minX, maxX + 1):
    y = (R**2 - (x-X)**2).sqrt()
    ans += math.floor(Y+y) - math.ceil(Y-y) + 1
    # print(x, math.floor(Y+y), math.ceil(Y-y))
print(ans)
