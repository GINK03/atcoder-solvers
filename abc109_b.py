
n = int(input())

word_set = set()

chaine = []
for i in range(n):
  w = input()
  word_set.add(w)
  if chaine == []: 
    chaine.append( w[0] + w[-1] )
  else:
    if chaine[-1][-1] == w[0]:
      chaine.append( w[0] + w[-1] )

if len(word_set) == n and len(chaine) == n:
  print('Yes')
else:
  print('No')
