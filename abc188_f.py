import collections

sys.setrecursionlimit(10**9)

X,Y=map(int,input().split())
val = collections.defaultdict(lambda : float('inf'))
minOps = abs(X-Y)

ans = []
# Yから減らすように考える
def dfs(num, ops):
    global minOps
    minOps = min(minOps, ops+abs(X-num))
    # 停止条件
    if minOps <= ops:
        return


    if num%2 == 0:
        dfs(num*2, ops+1)
    else:
        # 一増やす
        dfs((num+1)//2, ops+2)
        # 一減らす
        dfs((num-1)//2, ops+2)

dfs(Y,0)
print(minOps)
