from itertools import groupby
N, M = map(int, input().split())

classes =[]
for m in range(M):
    P, Y = map(int, input().split())
    classes.append( (P, Y) ) 

cr = {}
for key, cls in groupby(sorted(classes[:]), lambda x:x[0]):
    for i, (p, y) in enumerate(sorted(list(cls), key=lambda x:x[1])):
        cr[(p, y)] = i + 1

for P, Y in classes:
    rank = cr[(P, Y)]
    print(f'{P:06d}{rank:06d}')
