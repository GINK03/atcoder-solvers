import collections
import sys; sys.setrecursionlimit(10**9)

N = int(input())
*A,=map(int,input().split())

ans = 0; debug = []
def dfs(i, prt, acc):
    global ans, debug
    a = A[i]
    if i == N - 1:
        if prt == 0:
            ans = acc + a
        else:
            ans = acc - a
        return
    if a == 0:
        nprt = 0
        tmp = 0
        dfs(i+1, nprt, acc + tmp)
    elif prt == 0:
        tmp, nprt = max( [(a, 0), (-a, 1)] )
        dfs(i+1, nprt, acc + tmp)
    else:
        tmp, nprt = max( [(-a, 0), (a, 1)] ) 
        dfs(i+1, nprt, acc + tmp)

dfs(1, 0, A[0])
ans0 = ans

dfs(1, 1, -A[0])
ans1 = ans

print(max(ans0, ans1))
