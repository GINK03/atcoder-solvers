import sys; sys.setrecursionlimit(10**9)

N = int(input())

cnt = 0
def dfs(n):
    global cnt
    if n > N:
        return
    if set(str(n)) == {"7", "5", "3"}:
        cnt += 1 
    for k in [7, 5 ,3]:
        nn = 10*n + k
        dfs(nn)

for k in [7,5,3]:
    dfs(k)

print(cnt)
