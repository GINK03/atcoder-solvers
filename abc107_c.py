
N, K = map(int, input().split())

xs = [int(x) for x in input().split()] 

ans = 99999999999
for i in range(0,len(xs)-K+1):
  sliced = xs[i:i+K]
  head = abs(sliced[0])
  delta = sliced[-1] - sliced[0]
  ans = min(head+delta, ans)

print(ans)
