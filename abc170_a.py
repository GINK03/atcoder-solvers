
x5 = list(map(int, input().split()))

a = [idx+1 for idx, i in enumerate(x5) if i == 0]
print(a[0])
