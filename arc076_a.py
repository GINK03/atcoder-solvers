import os
from functools import reduce


a, b = map(int, input().split() )

aa = reduce(lambda y,x: y*x%1000000007, [i for i in range(1,a+1) ] )
bb = reduce(lambda y,x: y*x%1000000007, [i for i in range(1,b+1) ] )
if a == b :
  print(2*aa*bb%1000000007)
elif a+1 == b or a == b+1:
  print(aa*bb%1000000007)
else:
  print(0)

