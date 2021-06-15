
N,Q=map(int,input().split())
*A,=map(int,input().split())

Qs = [int(input()) for _ in range(Q)]
import bisect
for q in Qs:
    qi = bisect.bisect_right(A,q)
    #print(qi, A[qi])
    # 最小なのでそのまま出力
    if qi == 0:
        print(q)
        continue
    
    pqi = qi
    di = qi
    if qi > 0:
        while True:
            # インデックスの差分分足す
            q += di
            #print("aaa", q)
            qi = bisect.bisect_right(A,q)
            # 更新がなくなったらbreak
            if qi == pqi:
                print(q)
                break
            di = qi - pqi
            pqi = qi

