
N = int(input())


pf = set()
for i in range(1, int(N**0.5) + 1):
    if N%i == 0:
        pf.add(N//i)
        pf.add(i)

for p in sorted(pf):
    print(p)

