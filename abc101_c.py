
n, k = map(int, input().split())
xs = [int(x) for x in input().split()]

xs = sorted(xs)

min_ = min(xs)

cur = 0

for l in range(1, 100000):
  try:
    for j in range(xs[cur:].index(min_), k):
      xs[cur+j] = min_
    cur = cur + xs[cur:].index(min_)+k-1
    #print(cur)
    #print(xs)
  except:
    break
#print(xs)
print(l)
