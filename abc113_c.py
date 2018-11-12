from itertools import groupby

N, M = map(int, input().split())

classes = []

for m in range(M):
  P, Y = map(int, input().split())
  classes.append( (P, Y) ) 

classes_rank = {}
for key, cls in groupby(sorted(classes, key=lambda x:x[0]), lambda x:x[0]):
  for index, c in enumerate(sorted(list(cls), key=lambda x:x[1])):
    classes_rank[c] = index + 1

for cls in classes:
  P, Y = cls
  rank = classes_rank[ cls ]
  print('{P:06d}{rank:06d}'.format(P=P, rank=rank))
