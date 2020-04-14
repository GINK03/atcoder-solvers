n,q=map(int,input().split())

mtx = [['N']*n for n_ in range(n)]

for q_ in range(q):
    qs=list(map(int,input().split()))

    order = qs[0]
    if order == 1:
        s = qs[1]-1
        t = qs[2]-1
        mtx[s][t] = "Y"
    elif order == 2:
        s = qs[1]-1
        for n_ in range(n):
            if mtx[n_][s] == "Y":
                mtx[s][n_] = "Y"
    elif order == 3:
        s = qs[1]-1
        t_idxs = []
        for idx in [idx for idx, flag in enumerate(mtx[s]) if flag == "Y"]:
            t_idx = [idx for idx, flag in enumerate(mtx[idx]) if flag == "Y" and idx != s]
            t_idxs.extend(t_idx)
        for idx in t_idxs:
            mtx[s][idx] = "Y"

for a in mtx:
    print(''.join(a))
            
            

