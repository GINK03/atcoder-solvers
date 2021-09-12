
N, M = map(int, input().split())
*A, = map(int, input().split())
A = set(A)

ps = set()
def sieve_div(n):
    dp = [1]*(n+1) # 初期値ですべてを素数と仮定
    for i in range(2, n+1):
        if i in A:
            ps.add(i)

        flg = False

        if dp[i]: # もし素数ならば
            if i in A:
                flg = True
            j = 2 * i # iの倍数はすべて素数ではないはず
            while j <= n:
                dp[j] = 0
                if j in A:
                    flg = True
                j += i 
        if flg:
            ps.add(i)
            j = 2 * i # iの倍数はすべて素数ではないはず
            while j <= n:
                dp[j] = 0
                ps.add(j)
                j += i 
            
    return dp
sieve_div(10**5 + 100000)
ans = [i for i in range(1, M+1) if i not in ps]

print(len(ans))
for a in ans:
    print(a)
