import itertools
N,Q=map(int,input().split())
A=list(map(int, input().split()))
C=list(map(int, input().split()))

MOD=1000000007

X=[0]
for i in range(len(A)-1):
    X.append(pow(A[i], A[i+1], MOD))
X += [0, 0]

#print(X)
AC0 = list(itertools.accumulate(X))
AC1 = list(reversed(list(itertools.accumulate(reversed(X)))))
#print(AC0)
#print(AC1)

tmp = 1
acc = 0
for c in C + [1]:
    if c > tmp:
        acc += AC0[c-1] - AC0[tmp-1]
    else:
        acc += AC1[c] - AC1[tmp]
    acc %= MOD
    #print(tmp, c, acc)
    tmp = c
print(acc)

