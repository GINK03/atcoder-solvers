N = int(input())

s_ps = {}
for n in range(N):
    s,p=input().split()
    p=int(p)

    if s_ps.get(s) is None:s_ps[s] = []

    s_ps[s].append((n,p))

for s, ps in sorted(s_ps.items(), key=lambda x:x[0]):
    for n, p in sorted(ps, key=lambda x:x[1]*-1):
        print(n+1)
