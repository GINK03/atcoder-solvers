
import itertools
import numpy as np

def digit_dp(x):
    a = str(x)
    n = len(a)
    #配列は末から
    dp = np.zeros((11, 2, 11)).astype(int).tolist()
    dp[0][0][0] = 1
    # 条件に合わせてDP
    # 未満フラグ(less)は上の桁から成約を受けていないかを調べる <=> lessのときi桁までは全スキャン、lessでないときi桁はa[i]桁までしか見れない
    for i, less, num1 in itertools.product(range(n), (0,1), range(10)):
        max_d = 9 if less else int(a[i])
        for d in range(max_d+1):
            less_ = less or d < max_d
            num1_ = num1 + int(d == 1)
            dp[i + 1][less_][num1_] += dp[i][less][num1]

    #合致するものを合算
    ret = 0
    for less, num1 in itertools.product((0, 1), range(10)):
        '''num1になるものが何個あるのかを知りたいのでnum1を掛ける必要がある'''     
        ret += dp[n][less][num1]*num1
    return ret

A = int(input())
print(digit_dp(A))
