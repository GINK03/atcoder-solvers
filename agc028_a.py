from fractions import gcd
# https://img.atcoder.jp/agc028/editorial.pdf
N, M = map(int,input().split())
S = input()
T = input()

L = int((N*M)/gcd(N, M))

gcded = gcd(N,M)
n = N//gcded
m = M//gcded
for i in range(gcded):
  if S[i*n] != T[i*m]:
    print(-1)
    exit()

print(L)
