import math
MOD = 10**9+7
a,b = map(int,input().split())
a-=1; b-=1
print(math.factorial(a+b)//(math.factorial(a)*math.factorial(b))%MOD)
