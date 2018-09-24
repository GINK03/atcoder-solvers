N, M, X, Y = map(int, input().split())

xs = [int(x) for x in input().split()]
ys = [int(y) for y in input().split()]

res = False
for th in range(X+1, Y+1):
  is_up = all([x < th for x in xs ])
  is_down = all([y >= th for y in ys])
  
  #print(th, is_up, is_down)
  if is_up and is_down:
    res = True

print("No War" if res else "War")
