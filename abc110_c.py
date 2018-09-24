
S = input()
T = input()

s_shelv = [None for x in range(26)]
t_shelv = [None for x in range(26)]

a_z = list('abcdefghijklmnopqrstuvwxyz')


for i in range(len(S)):
  s = S[i]
  t = T[i]
  si = a_z.index(s)
  ti = a_z.index(t)

  if s_shelv[si] is None:
    s_shelv[si] = ti
  elif s_shelv[si] != ti:
    print('No')
    exit()

  if t_shelv[ti] is None:
    t_shelv[ti] = si
  elif t_shelv[ti] != si:
    print('No')
    exit()

print('Yes')
