
'''得点と考える
 1. 一回公演すると A + B人得る
 2. 対抗選手はAを機会損失する
 3. 1,2より2*A + Bが得点になる
'''
N=int(input())

A = []
acc_a = 0
for _ in range(N):
    a,b=map(int,input().split())
    score = 2*a + b
    acc_a += a
    A.append( (score, a, b) )
A.sort()
A=A[::-1]

cnt=0
acc = 0
for score, a, b in A:
    if acc > acc_a:
        break
    else:
        cnt += 1
        acc += a + b
        acc_a -=a

print(cnt)
    
