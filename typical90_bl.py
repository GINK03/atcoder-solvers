
N,Q=map(int,input().split())
*A,=map(int,input().split())

B = []
for i in range(N-1):
    B.append(A[i+1] - A[i])
ans = sum(abs(x) for x in B)

for q in range(Q):
    l, r, v = map(int, input().split())
    l-=1; r-=1
    if l-1 >= 0:
        prv_l = B[l-1]
        B[l-1] += v
        aft_l = B[l-1]
    else:
        prv_l = 0
        aft_l = 0
    if r < N-1:
        prv_r = B[r]
        B[r] -= v
        aft_r = B[r]
    else:
        prv_r = 0
        aft_r = 0

    ans += abs(aft_r) + abs(aft_l) - (abs(prv_r) + abs(prv_l))
    print(ans)
