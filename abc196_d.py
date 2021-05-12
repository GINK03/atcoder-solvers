

H, W, A, B = map(int, input().split())

ans = 0
def dfs(i, bit, A, B):
    global ans
    if i == H * W:
        ans += 1
        return 1
    if bit & (1<<i) > 0:
        dfs(i+1, bit, A, B)
        return None
    if B > 0:
        dfs(i+1, bit | 1<<i, A, B-1)
    if A > 0:
        # 右側に空きがありbitフラグが立っていないのであれば
        if i%W != W-1 and not (bit&(1 << (i+1)) > 0):
            dfs(i+1, bit | 1<<i | 1<<(i+1), A-1, B)
        # 下側に空きがああるのであれば
        if i+W < H*W:
            dfs(i+1, bit | 1<<i | 1<<(i+W), A-1, B)
    return None

r = dfs(0, 0, A, B)
print(ans)
