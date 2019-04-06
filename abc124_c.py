
Ss = [int(x) for x in list(input())]

A = [abs(i%2-x) for i,x in enumerate(Ss) ]
B = [abs((i+1)%2-x) for i,x in enumerate(Ss) ]
print(min([sum(A), sum(B)]))
