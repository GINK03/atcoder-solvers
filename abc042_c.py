
xs, k = input().split()

k = int(k)

xs = [int(x) for x in list(xs)]

ds = set([int(d) for d in input().split()])
#print(ds)
ans = []
for x in xs:
  if x not in ds:
    ans.append(x)
  else:
    us = [ u for u in range(0,10) if u not in ds ]    
    #print(us)
    x = sorted([ p for p in us if p > x ]).pop(0)
    ans.append(x)
print(''.join(map(str,ans)))
