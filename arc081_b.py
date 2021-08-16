import itertools
N = int(input())
S0 = input()
S1 = input()
MOD = 10**9 + 7

l = [len(list(vi)) for k, vi in itertools.groupby(S0)]

ans = 3*l[0]
for i in range(len(l)-1):
    if l[i] == 1 and l[i+1] == 1:
        ans *= 2
    if l[i] == 2 and l[i+1] == 2:
        ans *= 3
    if l[i] == 1 and l[i+1] == 2:
        ans *= 2
    if l[i] == 2 and l[i+1] == 1:
        ans *= 1
    ans %= MOD
print(ans)
