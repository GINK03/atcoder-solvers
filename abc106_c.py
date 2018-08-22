import sys
s = input()
k = int(input())

chrs = []
for ch in s:
  if int(ch) in {2,3,4,5,6,7,8,9}:
    chrs.append( (ch, 'Inf') )
  else:
    chrs.append( (ch, None) )

#print(chrs)

#で実数値がでるとき
#print( all(chrs[k2][1] is None for k2 in range(0,k)) )
if all(chrs[k2][1] is None for k2 in range(0,k)):
  print(1)
  sys.exit()
ret = None
for chr in chrs:
  if chr[1] == 'Inf':
    ret = chr[0]
    break

print(ret)
