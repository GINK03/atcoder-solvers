
N = int(input())
*V, = map(int, input().split())
A = V[:N]
B = V[N:]
import heapq
que = []

min_aoki = 0
for i in range(N):
    heapq.heappush(que, A[-i-1])
    heapq.heappush(que, B[i]) 
    min_aoki += heapq.heappop(que)

print(sum(V) - min_aoki)
