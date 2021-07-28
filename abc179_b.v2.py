N=int(input())


tmp  = [0]
for n in range(N):
    d1,d2 = input().split()
    if d1==d2:
        tmp.append(tmp[-1] + 1)
    else:
        tmp.append(0)

if max(tmp) >= 3:
    print("Yes")
else:
    print("No")
