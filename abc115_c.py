N, K = map(int, input().split())

ps = []
for n in range(N):
	ps.append(int(input()))
ps = sorted(ps)

mins = []

for start in range(N-K+1):
	mins.append( ps[start+K-1] - ps[start] ) 

print(min(mins))
