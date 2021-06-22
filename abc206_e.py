import collections

L, R = map(int,input().split())

def sieve():
    n = R
    dp = [1]*(n+1) # 初期値ですべてを素数と仮定
    dp[0] = 0; 
    dp[1] = 0
    nex = collections.defaultdict(int)
    for i in range(2, n+1):
        if dp[i]: # もし素数ならば
            nex[i] += 1
            j = 2 * i # iの倍数はすべて素数ではないはず
            while j <= n:
                dp[j] = 0
                nex[j] += 1
                j += i 

            j = i*i
            while j <= n:
                nex[j] = -10**9 - 7
                j += i*i 
    return nex

nex = sieve()

ans = 0
for i in range(2, R+1):
    if nex[i] < 0:
        continue
    cc = R//i - (L-1)//i # その数の倍数の個数
    if nex[i]%2 == 1: # 共通の素因数にならない個数(= 奇数の素因数の組み合わせ - 偶数の素因数の組み合わせ
        ans += (cc*(cc-1))//2
    else:
        ans -= (cc*(cc-1))//2

for i in range(max(2, L), R+1): # わかりやすい倍数を消去
    ans -= R//i - 1
print(ans*2)

