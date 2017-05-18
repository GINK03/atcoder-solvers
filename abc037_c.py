
m,n = map(int, input().split())
bs  = list( map(int, input().split()) )
size= len(bs)
a   = []
cnt = 1
for i,b in enumerate(bs):
  if i+1 < n:
    a.append( ((i+1), b))
  elif i > size - n:
    a.append( (n - cnt, b) )
    cnt+=1
  else:
    a.append( (n, b) )

print(sum(b*c for b,c in a))

