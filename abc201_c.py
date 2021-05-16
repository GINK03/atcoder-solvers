import itertools

S=input()

O=set([i for i,s in enumerate(S) if s=='o'])
X=set([i for i,s in enumerate(S) if s=='?'])
#exit()
cnt = 0
for t in itertools.product(list(O|X),repeat=4):
    a=set(t)
    if len(a&O) < len(O):
        continue
    #print(t)
    cnt += 1

print(cnt)
