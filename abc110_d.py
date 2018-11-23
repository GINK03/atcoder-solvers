from functools import reduce

N, M = map(int,input().split())
def factors(n):    
  res = []
  cur = 2
  #for i in range(2, int(n**0.5)+2):
  while True:
    if n%cur == 0:
      res.append(cur)
      n /= cur
      cur = 2
      continue
    cur += 1
    if n == 1: break
  return res

fs = factors(M)
#fs.append(1)

def C(n,r):
  a=1
  b=1
  for i in range(r):
    a=a*(n-i)
    b=b*(r-i)
  return((a//b)%(10**9+7))

from collections import Counter
c = dict(Counter(fs))

ans = 1
for fact in c:
  freq = c[fact]
  ans *= C(N+freq-1,freq) 
print(ans%((10**9)+7))
