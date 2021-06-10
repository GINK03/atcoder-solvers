

a,b,x=map(int,input().split())

import math
if a**2*b/2 > x:
    # y * a * b // 2 = x
    # -> y = 2 * x / (a * b)
    y = 2 * x / (a * b)
    # 長編 t = (y**2 + b**2) ** 0.5
    t = (y**2 + b**2) ** 0.5
    # sin theta = b/t
    rad = math.asin(b/t)
    print(math.degrees(rad))
else:
    print(math.degrees(math.atan((2*(a**2*b-x)/(a**3)))))
    
