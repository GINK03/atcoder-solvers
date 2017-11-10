import math

n = int(input())

a = []
if n==0:
  a.append('0')
while n!=0:
  if n%2 == 0:
    a.append('0')
  else:
    a.append('1')
    n-=1
  n //= -2

print(''.join(a[::-1]))
