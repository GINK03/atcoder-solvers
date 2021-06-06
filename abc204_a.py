
*xy,=map(int,input().split())
xy=set(xy)

if len(xy) == 1:
    print(list(xy)[0])
else:
    print(list({0,1,2} - xy)[0])
