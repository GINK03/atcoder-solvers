import re
n = int(input())

lens = []
for i in range(n):
  m = re.search(r'0{1,}$', input())  
  if m is None:
    lens.append(0) 
  else:
    lens.append( len(m.group(0)) )

print(min(lens))
