# 解けていないです！！（辛い）
N = int(input())
vs = [int(v) for v in input().split()]

e, o = {}, {}
for i, v in enumerate(vs):
  if i%2 == 0:
    if v in e:
      e[v] += 1
    else:
      e[v] = 1
  else:
    if v in o:
      o[v] += 1
    else:
      o[v] = 1

print(e)
print(o)

ts_e = sorted([(k,v) for k,v in e.items()], key=lambda x:x[1])[-2:]
ts_o = sorted([(k,v) for k,v in o.items()], key=lambda x:x[1])[-2:]

rep = 0
# case1. ke, koが同じ時
if ke == ko:
  if ve < vo:
    rep = ve
    print(rep)
    exit()
  else:
    rep = vo
    print(rep)
    exit()


    
    
