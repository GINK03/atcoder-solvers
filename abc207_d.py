

N = int(input())

AB = []
for _ in range(N):
    a,b =map(int,input().split())
    AB.append( (a,b) )
amean = sum([a for a, b in AB])
bmean = sum([b for a, b in AB])
AB = [(N*a-amean, N*b-bmean) for a, b in AB]

CD = []
for _ in range(N):
    c,d =map(int,input().split())
    CD.append( (c,d ) )

cmean = sum([a for a, b in CD])
dmean = sum([b for a, b in CD])
CD = [(N*c-cmean, N*d-dmean) for c,d in CD]


""" 原点は必ず0以外の点である必要がある """
""" 原点が0だと、そもそも相対角度にならないから！！ """
for i in range(N):
    if AB[i][0] != 0 or AB[i][1] != 0:
        AB[0], AB[i] = AB[i], AB[0]
        break

import math
def check(AB, CD):
    a, b = AB[0]
    for c, d in CD:
        angle = math.atan2(d,c) - math.atan2(b,a)
        acc = True
        for na,nb in AB:
            new_a = na*math.cos(angle) - nb*math.sin(angle)
            new_b = na*math.sin(angle) + nb*math.cos(angle)
            flag = False
            for tmp_c, tmp_d in CD:
                if abs(new_a - tmp_c) < 0.000001 and abs(new_b - tmp_d) < 0.000001:
                    flag = True
            acc &= flag

        if acc:
            print("Yes")
            exit()
    print("No")

check(AB, CD)
 

