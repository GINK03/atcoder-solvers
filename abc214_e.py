
import collections
import heapq
import bisect
T = int(input())

def main():
    N = int(input())
    LR = []
    for n in range(N):
        l, r = map(int, input().split())
        LR.append( (l, r))
    LR.sort(reverse=True)
    target = LR[-1][0]
    balls = []
    while LR or balls:
        if not balls:
            target = LR[-1][0]
        while LR and LR[-1][0] == target:
            l, r = LR.pop()
            heapq.heappush(balls, (r, l))
        r, l = heapq.heappop(balls)
        if r < target:
            print("No")
            return 
        target += 1
    print("Yes")



for t in range(T):
    main()
