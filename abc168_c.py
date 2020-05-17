a,b,h,m=map(int,input().split())
import math
hd = ((h%12)/12)*360 + 360/12 * m/60
md = ((m%60)/60)*360

c2 = a**2 + b**2 - 2*a*b*math.cos(2*math.pi * (abs(hd-md)/360))
# print(abs(hd-md))
# print(a**2 + b**2, math.cos(2*math.pi * (abs(hd-md)/360)))
# print(c2)
print(c2**0.5)
