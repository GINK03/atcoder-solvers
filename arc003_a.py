ins = input().strip()
if not ('S' in ins and 'N' in ins) and ('S' in ins or 'N' in ins):
	print('No')
	exit()
if not ('E' in ins and 'W' in ins) and ('E' in ins or 'W' in ins):
	print('No')
	exit()

print('Yes')
