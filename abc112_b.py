
N, T = map(int, input().split())

cts = []
for n in range(N):
  c, t = map(int, input().split())

  cts.append( (c,t)) 

cts = [(c,t) for c,t in cts if t <= T]

cts = sorted(cts, key=lambda x:x[0])

if len(cts) >= 1:
  print(cts[0][0])
else:
  print('TLE')
