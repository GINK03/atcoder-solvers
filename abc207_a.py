import itertools

*A,=map(int,input().split())

ans = 0
for ps in itertools.combinations(A,2):
    ans = max(sum(ps), ans)
print(ans)
