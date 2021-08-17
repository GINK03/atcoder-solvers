
import collections
import heapq
import bisect
import itertools
T = int(input())

def main():
    N = int(input())
    LR = []
    for n in range(N):
        l, r = map(int, input().split())
        LR.append((l, r))
    LR.sort(key=lambda x:x[0])
    TL = [l for l,r in LR]
    j = 0
    tmp = 0
    que = []
    for tl in TL:
        tmp = max(tl, tmp)
        while j < N and LR[j][0] <= tmp:
            heapq.heappush(que, LR[j][1])
            j += 1
        r = heapq.heappop(que)
        if r < tmp:
            print("No")
            return
        tmp += 1
    print("Yes")



for t in range(T):
    main()
