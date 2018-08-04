
s = input()
t = input()

alls = []
for sl in range(len(s)):
  alls.append(s[sl:] + s[:sl])

if t in alls:
  print('Yes')
else:
  print('No')
