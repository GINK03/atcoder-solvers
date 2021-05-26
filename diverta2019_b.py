
R,G,B,N=map(int,input().split())
# r = (N - Gg - Bb) / R

cnt = 0
for g in range(0,3001):
    for b in range(0, 3001):
        x = N - g*G - b*B
        if x%R == 0 and x/R >= 0:
            # print(x, g, b)
            cnt += 1
print(cnt)
