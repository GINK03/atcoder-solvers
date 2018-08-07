from collections import Counter

s = input()

head = s[0]
mid  = dict(Counter(s[2:-1]))
removed = s.replace('A', '').replace('C', '')
if head == 'A' and mid.get('C') is not None and mid['C'] == 1 and removed == removed.lower():
  print('AC')
else:
  print('WA')
  
