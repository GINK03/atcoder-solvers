
Es = [int(c) for c in input().split()]
B = int(input())
Ls = [int(c) for c in input().split()]

match = len(set(Es) & set(Ls))

res = 0
if match == 6:
	res = 1
elif match == 5 and B in Ls:
	res = 2
elif match == 5:
	res = 3
elif match == 4:
	res = 4
elif match == 3:
	res = 5

print(res)
