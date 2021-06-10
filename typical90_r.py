
T=int(input())
L,X,Y=map(int,input().split())
Q=int(input())

from math import sin, cos, sqrt, atan2, pi as PI, degrees
def query(I):
    cx = 0
    cy = -(L / 2.0) * sin(I / T * 2.0 * PI)
    cz = (L / 2.0) - (L / 2.0) * cos(I / T * 2.0 * PI)
    d1 = sqrt((cx - X) * (cx - X) + (cy - Y) * (cy - Y))
    d2 = cz
    kaku = atan2(d2, d1)
    return degrees(kaku)


for _ in range(Q):
    E = int(input())
    print(query(E))
