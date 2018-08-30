
s = input()
# curs = [index1, index2] 
curs = [0]
while True:
  next_curs = []
  break_ = False
  for c in curs:
    #print(c)
    if s[c:c+5] == 'dream':
      next_curs.append( c+5 )
      if len(s) == c+5:
        break_ = True
    if s[c:c+7] == 'dreamer':
      next_curs.append( c+7 )
      if len(s) == c+7:
        break_ = True
    if s[c:c+5] == 'erase':
      next_curs.append( c+5 )
      if len(s) == c+5:
        break_ = True
    if s[c:c+6] == 'eraser':
      next_curs.append( c+6 )
      if len(s) == c+6:
        break_ = True
  if next_curs == []:
    print('NO')
    break
  if break_: 
    print('YES')
    break
  curs = next_curs
