N,Y=map(int,input().split())

#A0
#A1
#A2
ans =[]
for a0 in range(N+1):
    b0 = 10000 * a0
    if 0>=N+1-a0 or b0 > Y:
        continue
    for a1 in range(N+1-a0):
        b1 = 5000*a1
        if 0>=N+1-a0-a1 or b0 + b1 > Y:
            continue
        a2 = N - a0 - a1
        if a2 >= 0 and 1000*a2 + b0 + b1 == Y:
            print(a0, a1, a2)
            exit()

print(-1, -1, -1)

