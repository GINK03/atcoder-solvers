

N, K = map(int, input().split())
MOD = 10**9 + 7
 
gcd_is_g = [0 for g in range(K+1)]
# gcd_is_g[g] ... gcd(A) = g となるような A の個数
 
ans = 0
for g in range(1, K+1)[::-1]:
  p = K//g
  
  # gcd(A) = c*g と書けるような A の個数を求める
  gcd_is_g[g] = pow(p, N, MOD)
  
  # gcd(A) = c*g (c>1) となるような A の個数を除く
  c = 2
  while g*c < K+1:
    gcd_is_g[g] -= gcd_is_g[g*c]
    c += 1
    
  gcd_is_g[g] %= MOD
    
    
  ans += gcd_is_g[g] * g
  ans %= MOD
  
print(ans)
