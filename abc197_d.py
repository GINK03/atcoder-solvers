# https://colab.research.google.com/drive/1KaETD6g6U2Rvge-9DQ8m5UhC_HR756iu?usp=sharing
import math
N = int(input())
x0,y0 = map(int,input().split())
x1,y1 = map(int,input().split())
d = math.sqrt((x1-x0)**2+(y1-y0)**2)/2
xo = (x0+x1)/2
yo = (y0+y1)/2
rad = math.atan2(y0-yo,x0-xo)
rad += math.radians(360/N)
xa = math.cos(rad)*d+xo
ya = math.sin(rad)*d+yo
print(xa,ya)
