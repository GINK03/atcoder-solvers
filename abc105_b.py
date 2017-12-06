
n = int(input())

s = set()
for i1 in range(26):
  for i2 in range(15):
    s.add( i1*4 + i2*7 )

if n in s:
  print('Yes')
else:
  print('No')
    
