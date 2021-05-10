import math
R,X,Y=map(int,input().split())

l2=X**2 + Y**2

lr = math.sqrt(l2)
# print(lr, math.ceil(lr))

if lr==R:
    print(1)
elif lr!=R and 2*R >= lr:
    print(2)
else:
    print(math.ceil(lr/R))
