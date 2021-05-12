
import collections
H, W, A, B = map(int, input().split())

def dfs():
    '''
    i: flattenした今いるindex
    bit: flattenしたmatrixの埋まり具合
    A, B: 一畳と半畳の畳の数
    '''
    ans = 0
    while que:
        i, bit, A, B = que.pop()
        if i == H * W:
            ans += 1
        if bit & (1<<i) > 0:
            # すでに埋まっていたら一つすすめる
            que.append( (i+1, bit, A, B) )
            continue
        if B > 0:
            # Bを使用する例
            que.append( (i+1, bit|1<<i, A, B-1) )
        if A > 0:
            # Aを使用する例
            # 右側に空きがありbitフラグが立っていないのであれば
            if i%W != W-1 and not (bit&(1 << (i+1)) > 0):
                que.append( (i+1, bit|1<<i|1<<(i+1), A-1, B) )
            # 下側に空きがああるのであれば
            if i+W < H*W:
                que.append( (i+1, bit|1<<i|1<<(i+W), A-1, B) )
    return ans
que = collections.deque([(0, 0, A, B)])
ans = dfs()
print(ans)
