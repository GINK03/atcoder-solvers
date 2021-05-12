
import math
N=int(input())

# 合成関数を作成する
top, buttom, fix = math.inf,-math.inf,0
for n in range(N):
    A,T=map(int,input().split())
    if T==1:
        top += A
        buttom += A
        fix += A
    if T==2:
        top = max(top, A)
        buttom = max(buttom, A)
    if T==3:
        top = min(top, A)
        buttom = min(buttom, A)
        
input()

def func(x):
    return max(buttom, min(top, x+fix))

for x in map(int,input().split()):
    print(func(x))
