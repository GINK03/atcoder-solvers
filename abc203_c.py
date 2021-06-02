

N,K=map(int,input().split())

AB = []
for _ in range(N):
    A, B = map(int,input().split())
    AB.append( (A,B) ) 
AB.sort()
#print("D", AB)

a0 = 0
AB2 = []
for i in reversed(range(0, len(AB))):
    a, b = AB[i]
    if i > 0:
        a -= AB[i-1][0]
    AB2.append( (a,b) )
    a0 = a
AB2 = list(reversed(AB2))

#print("D2", AB2)

acc = 0
for a, b in AB2:
    if K >= a:
        acc += a
        K -= a
        K += b
        # print(acc, K)
    elif K < a:
        #acc += K
        break
print(acc + K)



