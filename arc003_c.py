N, M = map(int,input().split())

tape = [ [ {'bright':-1, 'passed':None,  'type':None } for m in range(M) ] for n in range(N)]

cur = None
for n in range(N):
	for m, c in enumerate(input().strip()):
		if c == 'g' or c == 's':
			tape[n][m]['type'] = c
			if c == 'g':
				cur = [n, m]
		else:
			tape[n][m]['bright'] = float(int(c))

time = 0
scores = []
for _ in range(400):
	n, m = cur
	time += 1
	costs = []
	try:
		if n-1 >= 0 and m >= 0:
			a = tape[n-1][m] 
			cost = ( a['bright'], (n-1, m) )
			if a['type'] == 's':
				break
			if a['passed'] is None:
				costs.append(cost)
	except: ...
	try:
		if n+1 >= 0 and m >= 0:
			a = tape[n+1][m] 
			cost = ( a['bright'], (n+1, m) )
			if a['type'] == 's':
				break
			if a['passed'] is None:
				costs.append(cost)
	except: ...
	try:
		if n >= 0 and m-1 >= 0:
			a = tape[n][m-1] 
			cost = ( a['bright'], (n, m-1) )
			if a['type'] == 's':
				break
			if a['passed'] is None:
				costs.append(cost)
	except: ...
	try:
		if n >= 0 and m+1 >= 0:
			a = tape[n][m+1] 
			cost = ( a['bright'], (n, m+1) )
			if a['type'] == 's':
				break
			if a['passed'] is None:
				costs.append(cost)
	except: ...

	mm = max(costs, key=lambda x:x[0])
	scores.append(mm[0]) #*(0.99**time)
	#print(mm)
	tape[mm[1][0]][mm[1][1]]['passed'] = True
	cur = mm[1]

scores = scores[::-1]
#print(scores)
scores = [(0.99**(index+1))*score for index, score in enumerate(scores)]
print(min(scores))
