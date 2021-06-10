import collections
import heapq
N, K = map(int, input().split())
*V,=map(int, input().split())
# 左から取る回数をA
# 右から取る回数をBとする
ans = -float("inf")
for A in range(N+1):
    for B in range(N+1-A):
        if A+B > K:
            continue
        que = collections.deque(V.copy())
        gets = []
        for _ in range(A):
            heapq.heappush(gets, que.pop())
        for _ in range(B):
            heapq.heappush(gets, que.popleft())
        # 値が負のものを捨てられるだけ捨てる
        for _ in range(K-A-B):
            if gets:
                x = heapq.heappop(gets)
                if x > 0:
                    gets.append(x)
                    break
        ans = max(ans, sum(gets))
print(ans)


def miss0():
    """解答を参考に求めたが正しい結果が得られなかった
    pythonでリストの重複を厳密に管理しながら捜査するのは難しそう""'
    acts = []
    for A in range(k):
        for B in range(k):
            if A+B>k:
                break
            acts.append((A,B))

    ress = []
    for A, B in acts:
        if A!=0:
            left = vs[:A]
        else:
            left = []
        if B!=0:
            right = vs[-B:]
        else:
            right =[]
        #print(A, B, left, right)
        join = left+right
        join = sorted(join)
        for l in range(K-A-B+1):
            res = sum(join[l:])
            ress.append(res)
    print(max(ress))
