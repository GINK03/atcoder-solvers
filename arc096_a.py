import math
A,B,C,X,Y=map(int,input().split())

ans = []
# 普通に作る
ans.append(A*X+B*Y)

# 最小の方を組み換えで作る場合
minxy = min(X,Y)
tmp = minxy*2*C
if X>=Y:
    x = X-minxy
    tmp += x*A
else:
    y = Y-minxy
    tmp += y*B
ans.append(tmp)

# 最大の方を組み換えで作る(全部組み換えで作る)    
maxxy = max(X,Y)
ans.append(C*2*maxxy)

print(min(ans))

