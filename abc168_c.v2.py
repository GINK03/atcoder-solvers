from math import pi as PI, cos, sin, dist
A,B,H,M=map(int,input().split())


# 60分で一回転するから60のmodが現在の示す角度
mrad = M%60/60 * 2*PI
mcos, msin = cos(mrad) * B, sin(mrad) * B

# 12時間で一回転するから12のmodが現在の示す角度
hrad = (H%12 + M/60)/12 * 2 * PI
hcos, hsin = cos(hrad)*A, sin(hrad) *A
print(dist((mcos, msin), (hcos, hsin)))
