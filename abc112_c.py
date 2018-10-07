
N = int(input())

xy_h = { }
for n in range(N):
  x,y,h = map(int, input().split())
  key = (x,y)
  xy_h[key] = h

for sx in range(100+1):
  for sy in range(100+1):
    
    rhs = []
    for xy, h in xy_h.items():
      x,y = xy
      if h == 0L
        rh = h + abs(x - sx) + abs(y - sy)
        rhs.append(rh)
    check = all( [ x == rh for x in rhs ] )
    #print(sx, sy, rh, check) 
   
    if check is True:
      print(sx, sy, rh) 
      exit()
    
