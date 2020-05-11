a,b,c,k=map(int,input().split())

if a >= k:
    r = k
elif a+b >= k:
    r = a
elif a+b+c >= k:
    r = a - (k-a-b)

print(r)
