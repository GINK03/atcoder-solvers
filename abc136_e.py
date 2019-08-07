N, K = map(int,input().split())

Xs = list(map(int,input().split()))

for l in reversed(range(1,max(Xs)+K+1)):
    vari = []
    for x in Xs:
        #if abs(2*x%l-l) > K:
        #    vari = []
        #    break
        vari.append( (x%l, l-x%l) )
    if vari != []:
        sum1 = sum([v[0] for v in vari])
        sum2 = sum([v[1] for v in vari])
        max2 = min([v[1] for v in vari])
        if sum1 == sum2 and max2 <= K and len(Xs) == 2:
            print(l)
            #print(l, vari, sum1, sum2)
            exit() 
        elif sum1 != sum2 and sum1%l == 0 and sum2%l == 0:
            print(l)
            #print(l, vari, sum1, sum2)
            exit()
        #print(l, vari, sum1, sum2)
...
