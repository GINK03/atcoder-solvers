
N,T=map(int,input().split())
*TS,=map(int,input().split())

TMP = []
for ts in TS:
    TMP.append( (ts, 1) ) 
    TMP.append( (ts+T, -1) )

TMP.sort()
#print(TMP)
acc = 0
st = 0
prv_ts = 0
for ts, flg in TMP:
    if st >= 1:
        acc += ts - prv_ts
    prv_ts = ts
    if flg == 1:
        st += 1
    else:
        st -= 1

print(acc)
