from itertools import combinations

N = int(input())

lists = []
for n in range(N):
	x, y = map(int, input().split())
	lists.append((x,y))

anss = []
for e1, e2 in combinations(lists,2):
	a = ((e1[0] - e2[0])**2 + (e1[1] - e2[1])**2)**0.5
	anss.append(a)

print(max(anss))
