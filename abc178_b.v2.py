import itertools
a,b,c,d=map(int,input().split())
print(max(x*y for x, y in itertools.product((a,b), (c,d))))





