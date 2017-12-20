
N, K = map(int, input().split())

ds = [int(d) for d in input().split()]

us = [ i for i in range(10) if i not in ds]
#print(us)

oo = [int(s) for s in str(N)]

o_u = {}
for o in oo:
  o_u[o] = min(list(filter(lambda x:x>=o, us)))

n = str(N)
for o, u in o_u.items():
  n = n.replace(str(o),str(u))

print(n)
