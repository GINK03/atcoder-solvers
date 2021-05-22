import itertools
N=int(input())
A=tuple(map(int,input().split()))
B=tuple(map(int,input().split()))

lst = []
for i, p in enumerate(itertools.permutations(range(1,N+1))):
    lst.append(p)
lst.sort()


for i, p in enumerate(lst):
    if p == A:
        a = i
    if p == B:
        b = i
print(abs(b-a))

