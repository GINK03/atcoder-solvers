import numpy as np

H,W = map(int, input().split())

arr = np.zeros((H,W), dtype=np.object)

for h in range(H):
  chars = input()
  for w in range(W):
    #print(chars[w])
    arr[h, w] = chars[w]
h_replace = []
for h in range(H):
  if all([a == '.' for a in arr[h]]):
    h_replace.append( h )

w_replace = []
for w in range(W):
  if all([a == '.' for a in arr[:,w]]):
    w_replace.append( w )

arr = np.delete(arr, h_replace, axis=0)
arr = np.delete(arr, w_replace, axis=1)
[ print(''.join(ar)) for ar in arr.tolist() ]
