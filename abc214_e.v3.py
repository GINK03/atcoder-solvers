
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
    LR.sort()
    tmp = 0
    for l,r in LR:
        tmp = max(l, tmp)
        # print(l, r, tmp)
        if tmp > r:
            print("No")
            return 
        tmp += 1 # 
    print("Yes")




for t in range(T):
    main()
