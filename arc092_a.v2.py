N = int(input())

red = [list(map(int,input().split())) for _ in range(N)]
blue = [list(map(int,input().split())) for _ in range(N)]
"""考え方; (x,y)でソートしたblueで、redは条件を満たす中で最もyが大きいものを選ぶ"""

"""blueをソートする x, yの順"""
blue.sort()

"""redをソートする -y,xの順"""
red.sort(key=lambda x: (-x[1], x[0]))


matchs = set()
for bx, by in blue:
    for ax, ay in red:
        if ax < bx and ay < by:
            if (ax, ay) in matchs:
                continue
            else:
                matchs.add( (ax, ay) )
                break
print(len(matchs))
            
