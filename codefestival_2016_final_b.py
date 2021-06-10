
N=int(input())


def greedy():
    use = set()
    for i in range(1, 10**7+1):
        if N >= i:
            if N-i not in use:
                use.add(i)
                N-=i
            if N == 0:
                break
    for i in use:
        print(i)

if N in {1, 2}:
    print(N)
    exit()

c = 0
for n in range(1, N+1):
    if N < n*(n+1)//2:
        c = n
        break
d = c*(c+1)//2 - N

for a in range(1, c+1):
    if a == d:
        continue
    print(a)

