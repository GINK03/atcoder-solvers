

N=int(input())
DCS=[]
for _ in range(N):
    *dcs,=map(int,input().split())
    DCS.append(dcs)
DCS.sort()

time = 0
acc = 0
for d,c,s in DCS:
    if time + c <= d:
        time += c
        acc += s

print(acc)

