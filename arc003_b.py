N = int(input())

l = []
for n in range(N):
	line = input().strip()[::-1]
	l.append(line)

for line in sorted(l):
	print(line[::-1])
