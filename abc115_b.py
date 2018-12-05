N = int(input())

ps = []
for n in range(N):
	ps.append( (n, int(input())) )	

maxed = max(ps, key=lambda x:x[1])
maxed_index = maxed[0]
ps.pop(maxed_index)

b = maxed[1]/2
for p in ps:
	b += p[1]
print(int(b))
