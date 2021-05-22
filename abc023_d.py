import numpy as np
N = int(input())
HS = [list(map(int, input().split())) for _ in range(N)]
HS = np.array(HS)
H = HS[:,0]
S = HS[:,1]
 
def check(mid):
    # midの高さで撃った時、各々の風船はどれくらいの時間で撃てるか
    time = (mid-H)/S
    time.sort()
    # 最短手で撃っていった時、midの高さかそれ以上で撃てるはずである
    # 成立しないときはそもそも撃つことができない(ほど低い高度である)
    if ((time - np.array(list(range(N))) < 0)).any():
        return False
    return True

ng = 0
ok = 10**20
while ok - ng != 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid
 
print(ok)
