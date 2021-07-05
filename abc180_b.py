
N = int(input())
*X,=map(int,input().split())

m1 = sum([abs(x) for x in X])
m2 = sum([x**2 for x in X])**0.5
m3 = max([abs(x) for x in X])

print(m1)
print(m2)
print(m3)
