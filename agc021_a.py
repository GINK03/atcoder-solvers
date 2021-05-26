
N=input()

b = sum([int(n) for n in N])
a = int(N[0])-1 + 9*(len(N) - 1)
print(max(a,b))

