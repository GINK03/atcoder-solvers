import itertools

xs = list(map(int, input().split()))

anss = []
for ps in itertools.permutations(xs, len(xs)):
  ps = list(ps)
  head = ps[0]
  ps2 = ps.copy()
  ps2.insert(0, 0)
  s = [abs(a-b) for a, b in list(zip(ps, ps2))]
  #print(s, head)
  anss.append(sum(s)-head)
print(min(anss))
