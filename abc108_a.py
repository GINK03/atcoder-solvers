
k = int(input())

ans = set()
for i1 in range(1,k+1):
  for i2 in range(1,k+1):
    if i1%2 == 0 and i2%2 == 1:
      ans.add( (i1, i2) )      
print(len(ans))
