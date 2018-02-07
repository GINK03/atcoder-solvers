
# 境界域だけを見ていく方法
# これは思いつかないので、知っておく
N, Q = map(int, input().split())
imos = [0] * N
for q in range(Q):
  l, r = map(int, input().split())
  imos[l - 1] += 1
  if r < N:
    imos[r] += -1
 
x = 0
a = ''
for i in imos:
  x += i
  if x % 2 == 0:
    a += '0'
  else:
    a += '1'

print(a)
