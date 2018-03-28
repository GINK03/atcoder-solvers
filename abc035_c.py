
N, Q = map(int, input().split())

ns = [0 for n in range(N)]
for q in range(Q):
  l,r = map(lambda x:int(x)-1, input().split())
  for m in range(l,r+1):
    ns[m] += 1
  #print(ns)
#print(ns)

def sw(x):
  if x%2 == 0: return '0'
  else: return '1'
ns = [ sw(x) for x in ns ]
print(''.join(ns))
