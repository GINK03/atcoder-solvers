import heapq
import collections
N, M = map(int, input().split())

dg = collections.defaultdict(list)
for n in range(N):
    day, gain = map(int, input().split())
    dg[day].append(gain)

que = []
ans = 0
for m in range(1, M + 1):  # 最後の日から見ていく
    for gain in dg[m]:
        heapq.heappush(que, -gain)
    if que:
        ans += -heapq.heappop(que)
print(ans)
