import math
s = input()

n = len(s)

def is_kaibun(s):
    n = len(s)
    h = s[0:math.ceil((n-1)/2)]
    t =  s[(n+3)//2-1:n]
    #print(h,t)
    return h == t[::-1]

h = s[0:(n-1)//2]
t =  s[(n+3)//2-1:n]

if is_kaibun(s) and is_kaibun(h) and is_kaibun(t):
    print("Yes")
else:
    print("No")
#print(h)
#print(t[::-1])
