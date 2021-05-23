import itertools

s=int(input())

l=[s]
def f(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1

ansi = {s:1}
for i in itertools.count(2):
    ans = f(l[-1])
    l.append(ans)
    if ans in ansi:
        print(i)
        break
    ansi[ans]=i
