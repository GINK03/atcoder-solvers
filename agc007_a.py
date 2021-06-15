
H,W = map(int,input().split())
cnt = 0
for h in range(H):
  cnt += input().count("#")
if cnt == H + W - 1:
  print('Possible')
else:
  print('Impossible')
