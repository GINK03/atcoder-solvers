def I():
    return int(input())


def MI():
    return map(int, input().split())


def LI():
    return list(map(int, input().split()))


n, W = MI()
v = []
w = []
for i in range(n):
    a, b = MI()
    v.append(a)
    w.append(b)

# n<=30 半分全列挙
def solve1():
    # 前半
    a = n // 2
    pre = []
    for i in range(2 ** a):
        sv = 0
        sw = 0
        for j in range(a):
            if (i >> j) & 1:
                sv += v[j]
                sw += w[j]
        pre.append((sw, sv))
    pre.sort()  # 重さ順
    # 後半
    b = n - a
    post = []
    for i in range(2 ** b):
        sv = 0
        sw = 0
        for j in range(b):
            if (i >> j) & 1:
                sv += v[a + j]
                sw += w[a + j]
        post.append((sw, sv))
    post.sort()  # 重さ順
    # print(pre,post)
    w_max = W

    def choice(lst):
        ans = [(0, 0)]
        sv = 0
        for w, v in lst:
            if w > w_max:
                break
            if v > sv:
                sv = v
                ans.append((w, v))
        return ans

    left = choice(pre)
    right = choice(post)
    # print(left,right)
    # 前半と後半から一つずつ取り出す
    ans = 0
    for w1, v1 in left:
        for w2, v2 in right:
            if w1 + w2 > W:
                break
            ans = max(ans, v1 + v2)
    print(ans)


# 計算量 (nw)
def solve2():
    # dp[i][sum_w]: i-1番目までの品物の重さがsum_wを超えないように選んだときの、価値の総和の最大値
    dp = [[0] * (W + 1) for i in range(n + 1)]
    for i in range(n):
        for j in range(W + 1):
            if j - w[i] >= 0:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j], dp[i][j - w[i]] + v[i])
            else:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
    print(max(dp[-1]))


# 計算量 (n^2 v) # v = max(v[i])
def solve3():
    inf = 10 ** 17
    mv = sum(v) + 10
    # dp[i][sum_v]: i-1番目までの品物の価値がsum_vとなるように選んだときの、重さの総和の最小値
    dp = [[inf] * mv for i in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(mv):
            if j - v[i] >= 0:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j], dp[i][j - v[i]] + w[i])
            else:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
    for i in range(mv):
        j = mv - 1 - i
        if dp[-1][j] <= W:
            print(j)
            break


if n <= 30:
    solve1()
elif max(w) <= 1000:
    solve2()
else:
    solve3()
