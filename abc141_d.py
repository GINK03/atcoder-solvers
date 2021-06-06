
import heapq
N,M=map(int,input().split())
*A,=map(int,input().split())
A=[(-a,a) for a in A]
heapq.heapify(A)

for mcnt in range(M):
    w, a = heapq.heappop(A)
    na = a//2
    heapq.heappush(A, (-na,na))

#print(A)
print(sum([a[1] for a in A]))

    
