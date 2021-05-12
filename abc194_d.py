N=int(input())

a = 0
for i in range(1,N):
    a += 1/((N-i)/N)
print(a)
