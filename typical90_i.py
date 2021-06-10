import itertools
import numpy as np
import bisect

def angle(c0, c1):
    cosine_angle = np.dot(c0, c1) / (np.linalg.norm(c0) * np.linalg.norm(c1))
    angle = np.arccos(cosine_angle)
    return np.degrees(angle)


def slow():
    N=int(input())
    XY = []
    for _ in range(N):
        x, y = map(int,input().split())
        XY.append( [x,y] )
    XY=np.array(XY)
    for a,b,c in itertools.permutations(XY,3):
        print(a, b, c, angle(a-c, b-c))
# slow()
    
def main():
    N=int(input())
    XY = []
    for _ in range(N):
        x, y = map(int,input().split())
        XY.append( [x,y] )
    XY=np.array(XY)
     

    ans = 0
    for c_pos in range(N):
        c = XY[c_pos]
        xy = [angle(x,c) for x in XY]
        print(c, xy)
        xy.sort()
        
        for i in range(len(xy)):
            a = xy[i]
            can_b = a + 180 
            if can_b >= 360:
                can_b -= 360
            i0 = bisect.bisect_left(xy, can_b)%len(xy)
            print( can_b, i0, xy[i0] - a)
            ans = max(xy[i0] - a, ans)
    print(ans)

main()
