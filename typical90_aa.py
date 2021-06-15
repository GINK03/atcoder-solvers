
N=int(input())
a=set()
for i in range(N):
    s=input()
    if s in a:
        continue
    else:
        a.add(s)
        print(i+1)

