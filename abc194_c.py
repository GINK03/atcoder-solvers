N=int(input())
A=list(map(int,input().split()))

left = N*sum([a**2 for a in A])
right = sum(A)**2
print(left-right)


