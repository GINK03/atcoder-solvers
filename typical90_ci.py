import copy
N, P, K = map(int, input().split())

G = [list(map(int, input().split())) for n in range(N)]

def eval(num):
    tmp = copy.deepcopy(G)
    for i in range(N):
        for j in range(N):
            if tmp[i][j] == -1:
                tmp[i][j] = num
    for k in range(0, N):
        for x in range(0, N):
            for y in range(0, N):
                tmp[x][y] = min(tmp[x][y], tmp[x][k] + tmp[k][y])
    cnt = 0
    for x in range(N):
        for y in range(N):
            if tmp[x][y] <= P:
                cnt += 1
    return cnt 



