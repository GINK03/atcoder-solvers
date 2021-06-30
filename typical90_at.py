
N=int(input())
*A,=map(int,input().split())
*B,=map(int,input().split())
*C,=map(int,input().split())

*A,=map(lambda x:x%46, A)
*B,=map(lambda x:x%46, B)
*C,=map(lambda x:x%46, C)

import collections

A = collections.Counter(A)
B = collections.Counter(B)
C = collections.Counter(C)


ans = 0
for ak in A.keys():
    for bk in B.keys():
        for ck in C.keys():
            if (ak+bk+ck)%46 == 0:
                ans += A[ak]*B[bk]*C[ck]
print(ans)
