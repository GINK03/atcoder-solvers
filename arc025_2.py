
class Cumsum2d:
    dp: "Optional[List[List]]" = None
    @staticmethod
    def generate(h, w, a):
        '''da[i][j]:(0,0)~(i,j)の長方形の和'''
        Cumsum2d.dp = dp = [[0]*w for j in range(h)]
        dp[0][0] = a[0][0]
        for i in range(1,w):
            dp[0][i] = dp[0][i-1]+a[0][i]
        for i in range(1,h):
            cnt_w = 0
            for j in range(w):
                cnt_w += a[i][j]
                dp[i][j] = dp[i-1][j]+cnt_w
        return dp
    @staticmethod
    def calc(p, q, x, y):
        dp = Cumsum2d.dp
        '''da_calc(p,q,x,y):(p,q)~(x,y)の長方形の和'''
        if p > x or q > y:
            return 0
        if p == 0 and q == 0:
            return dp[x][y]
        if p == 0:
            return dp[x][y]-dp[x][q-1]
        if q == 0:
            return dp[x][y]-dp[p-1][y]
        return dp[x][y]-dp[p-1][y]-dp[x][q-1]+dp[p-1][q-1]

import itertools

H,W=map(int, input().split())

C = [list(map(int, input().split())) for _ in range(H)]
for h,w in itertools.product(range(H), range(W)):
        if (h+w)%2==0: # ブラックチョコならば
            C[h][w] *= -1 # 正負を反転


Cumsum2d.generate(H,W,C)

ans = 0
for p, q in itertools.product(range(H), range(W)):
    for x, y in itertools.product(range(p, H), range(q, W)):
        if Cumsum2d.calc(p,q,x,y) == 0:
            ans = max(ans, (x-p+1)*(y-q+1))
print(ans)

