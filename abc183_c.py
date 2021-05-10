import itertools

N, K = map(int, input().split())

M = [list(map(int, input().split())) for n in range(N)]

res = 0
for p in itertools.permutations(range(2, N+1), N-1):
    b = [1] + list(p) + [1]

    calc = 0
    for i in range(len(b)-1):
        start, end = b[i:i+2]
        calc += M[start-1][end-1]
    # print(calc, b)
    if calc == K:
        res += 1
print(res)
