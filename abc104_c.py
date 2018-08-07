
D, G = map(int, input().split()) 

def gen(i, p, c):
  it = [ (0,0) ]
  for _p in range(p):
    if _p == p-1:
      it.append( (c + (i+1)*(_p+1)*100, _p+1) )
    else:
      it.append( ((i+1)*(_p+1)*100, _p+1) )
  return it

its = []
for i in range(D):
  p, c = map(int, input().split())
  it = gen(i, p, c)
  its.append( it )
from functools import reduce
import copy
ps = [ [0, 0] ]
for it in its:
  size = len(it)
  ps_next = []
  for p in ps:
    for cur in range(size): 
      pp    = copy.copy(p)
      pp[0] += it[cur][0]
      pp[1] += it[cur][1]
      ps_next.append( pp )

  score_freqs = {}
  for score, freq in ps_next:
    if score_freqs.get(score) is None:
      score_freqs[score] = []
    score_freqs[score].append( freq )

  ps_next = [[score, min(freqs)] for score, freqs in score_freqs.items()]
  ps = ps_next
#sys.exit()
ps = [ p for p in ps if p[0] >= G]
#print(ps)
print( min(ps, key=lambda x:x[1])[1] )
