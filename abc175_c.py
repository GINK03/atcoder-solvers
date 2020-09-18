import os

x,k,d=map(int,input().split())

x = abs(x)

ri=x//d
if ri <= k:
    nkr = k-ri
    if nkr%2==0:
        print(abs(x - ri*d))
    else:
        riso_a = abs(x-ri*d)
        print(min(abs(riso_a+d), abs(riso_a-d)))
elif ri > k:
   print(x - k*d) 
