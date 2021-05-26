k, a, b = map(int,input().split())
if b-a > 2:
    if k < a:
        print(k+1)
    else:
        k -= (a-1)
        print(a+(k//2)*(b-a) + (k%2))
else:
    print(k+1)

