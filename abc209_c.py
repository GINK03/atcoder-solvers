

MOD = 10**9 + 7
N = int(input())
*C,=map(int,input().split())

C.sort()
cmax = C[0]
cnt = 0
acc = 1
for i in range(N):
    c = C[i]
    diff_c = c - cmax
    if diff_c > 0:
        pat0 = cmax - cnt
        acc *= (diff_c + pat0) 
        #print(diff_c, pat0)
    else:
        acc *= (c - cnt)

    acc %= MOD
    cmax = max(c, cmax)
    cnt += 1

print(acc%MOD)

