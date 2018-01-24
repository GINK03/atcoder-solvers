
s = input()
T = input()
qs = []
for i, c in enumerate(s):
  if c == '?':
    qs.append( i )

import copy
blocks = [ list(s) ]
for qi in qs:
  _blocks = list()
  for _block in blocks:
    for ch in ['L', 'R', 'U', 'D']:
      cp = copy.copy(_block)
      cp[qi] = ch
      _blocks.append( cp )
    #print(_blocks)
  blocks = _blocks

#print(blocks)

xsc = []
for block in blocks:
  xs = [0,0]
  for ch in block:
    if ch == 'L': xs[0] -= 1
    if ch == 'R': xs[0] += 1
    if ch == 'U': xs[1] += 1
    if ch == 'D': xs[1] -= 1
  #print(xs)
  xsc.append( sum([abs(x) for x in xs]) )

if T == '1':
  print(max(xsc))
else:
  print(min(xsc))
