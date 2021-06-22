

A,B,C=map(int,input().split())

MOD = 998244353
acc = 1
for e in [A,B,C]:
    acc *= e * (e+1) // 2 
    acc %= MOD

print(acc)
