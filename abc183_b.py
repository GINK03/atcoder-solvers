import os

Sx, Sy, Gx, Gy = map(int, input().split())

Gy = - Gy
x = (0 - Sy)*(Gx - Sx)/(Gy - Sy) + Sx 
print(x)
