import itertools
A,B=map(int,input().split())

for cnt in itertools.count(0):
    if cnt*(A-1) + 1 >= B:
        break
print(cnt)
