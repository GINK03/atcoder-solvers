import itertools

N,A,B,C=map(int,input().split())
L = [int(input()) for _ in range(N)]



ans = (float('inf'),)
buff = []
for p in itertools.product(*[list(range(0, 4)) for _ in range(N)]):
    ai = [i for i,x in enumerate(p) if x == 1]
    bi = [i for i,x in enumerate(p) if x == 2]
    ci = [i for i,x in enumerate(p) if x == 3]
    
    size = 10*(len(ai) + len(bi) + len(ci))
    a = sum([L[i] for i in ai])
    b = sum([L[i] for i in bi])
    c = sum([L[i] for i in ci])
    
    if min(a, b, c) > 0: # 必ず一回はもとがなくてはだめ, 無からは生成できない
        cost = size + abs(A-a) + abs(B-b) + abs(C-c) - sum([a > 0, b > 0, c > 0])*10
        ans = min(ans, (cost, a, b, c, p))

print(ans)
