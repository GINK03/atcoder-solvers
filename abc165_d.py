
A,B,N=map(int,input().split())
import math
def f(x):
    return math.floor(A*x/B) - A*math.floor(x/B)


print(f(min(B-1,N)))

