x=int(input())

s=100

from itertools import count

for c in count(0):
    if s >= x:
        print(c)
        exit()
    s = int(s * 1.01)

