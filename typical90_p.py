
N=int(input())
A,B,C=map(int,input().split())

ans = float('inf')
for b in range(9999+1):
    for c in range(9999+1):
        if (N-(b*B + c*C)) >= 0 and (N-(b*B + c*C))%A == 0:
            a = (N-(b*B + c*C))//A
            ans = min(ans, a+b+c)
print(ans)
