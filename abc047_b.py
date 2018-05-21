import numpy as np
W, H, N = map(int, input().split())

z = np.zeros( (H, W) )
#print(z)

for n in range(N):
  x,y,a = map(int, input().split())

  if a == 1:
    z[:, :x] = 1

  if a == 2:
    z[:, x:] = 1

  y = H - y
  if a == 3:
    z[y:,:] = 1
  
  if a == 4:
    z[:y,:] = 1
#print(z)

ans = int(W*H - z.sum())
print(ans)
