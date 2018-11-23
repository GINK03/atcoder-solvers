
X, Y, W = input().split()

cs = [list(input()) for i in range(9)]

v = []
if 'R' == W:
	v = [1, 0]
elif 'L' == W:
	v = [-1, 0]
elif 'U' == W:
	v = [0, -1]
elif 'D' == W:
	v = [0, 1]
elif 'RU' == W:
	v = [1,-1]
elif 'RD' == W:
	v = [1,1]
elif 'LU' == W:
	v = [-1,-1]
elif 'LD' == W:
	v = [-1, 1]

start = [int(X)-1, int(Y)-1]

buff = []
for i in range(4):
	buff.append(cs[start[1]][start[0]])
	if i != 0:
		if start[1] >= 8 or start[1] <= 0:
			v[1] = v[1]*-1
		if start[0] >= 8 or start[0] <= 0:
			v[0] = v[0]*-1

	start[1] += v[1]
	start[0] += v[0]
	
print(''.join(buff))
