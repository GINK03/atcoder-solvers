

N=int(input())

S=[]
for _ in range(N):
    S.append(int(input()))
S.sort()

max_a = sum(S)
if max_a%10 == 0:
    for s in S:
        if s%10 != 0:
            print(max_a - s)
            exit()
        else:
            continue
    print(0)

else:
    print(max_a)
        


