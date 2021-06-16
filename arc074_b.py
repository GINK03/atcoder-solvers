
import heapq
import collections

N = int(input())
*A, = map(int,input().split())
A1 = A[:N]
A2 = collections.deque(A[N:2*N])
A3 = A[2*N:]
 
M = [0]*(N+1)
M[0] = sum(A1)

heapq.heapify(A1)
for i in range(N):
    s = M[i]
    t = heapq.heappop(A1)
    s -= t
    t2 = max(t,A2.popleft())
    s += t2
    heapq.heappush(A1,t2)
    M[i+1] = s
 
A2 = collections.deque(A[N:2*N])
A3 = [-a for a in A3]
m = [0]*(N+1)
m[0] = -sum(A3)
heapq.heapify(A3)
 
for i in range(N):
    s = m[i]
    t = -heapq.heappop(A3)
    s -= t
    t2 = min(t,A2.pop())
    s += t2
    heapq.heappush(A3,-t2)
    m[i+1] = s

ans = -float("inf") 
for i in range(N+1):
    ans = max(ans,M[i]-m[-i-1])
 
print(ans)
