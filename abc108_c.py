
N, K = map(int, input().split(' '))

nn = []
for i in range(3):
  for n in range(1, N+1):
    nn.append(n)

#print(nn)

import itertools

sss = set()
ssd = set()
for t in itertools.permutations(nn, 3):
  #print(t)
  a, b, c = tuple(sorted(t))
  if (a+b)%K == 0 and (b+c)%K == 0 and (c+a)%K == 0:
    sss.add(tuple(sorted(t)))
  else:
    ssd.add(tuple(sorted(t)))



print(sss)
