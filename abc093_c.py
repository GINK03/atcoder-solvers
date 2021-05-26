
A=list(map(int,input().split()))


a_max = max(A)
tmp = [a_max-a for a in A]
tmp.sort()
second = tmp[1]
third = tmp[2] - second

if third%2 != 0:
    print(second + third//2 + 2)
else:
    print(second + third//2)
