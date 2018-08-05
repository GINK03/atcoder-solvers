

from bisect import bisect
n, q = map(int, input().split())
x = list(map(int, input().split()))
x_sum = [0] * (n + 1)
for i in range(n):
  x_sum[i+1] = x_sum[i] + x[i]
 
def search(c, d):
  return bisect(x, c-d), bisect(x, c), bisect(x, c+d)
 
for _ in range(q):
  c, d = map(int, input().split())
  left, center, right = search(c, d)
  ans = 0
  ans += (2 * center - left - right) * c
  ans += x_sum[right] - x_sum[center] - (x_sum[center] - x_sum[left])
  ans += d * (n - (right - left))
  print(ans)
