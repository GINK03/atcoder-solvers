N,L=map(int,input().split())

ns=[i+L for i in range(N)]

min_idx = -1
mins = None
for idx, n in enumerate(ns):
    if mins is None:
        mins = abs(n)
        min_idx = 0
    else:
        if mins > abs(n):
            min_idx = idx
            mins = abs(n)

ns.pop(min_idx)
print(sum(ns))
