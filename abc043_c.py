
range_ = range(-100, 100+1)

n = int(input())

sb = { index:None for index in range_ }

xs = [int(x) for x in input().split()]

def delfun(arg):
  xs, delta = arg
  deltas = sum( [ (x-delta)**2 for x in xs] )
  return deltas

from concurrent.futures import ProcessPoolExecutor as PPE

res = PPE(max_workers=12).map(delfun, [(xs, delta) for delta in range_])
print(min(list(res)))


