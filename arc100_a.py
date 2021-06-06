import statistics
N=int(input())
*A,=map(int,input().split())
B = [A[n]-(n+1) for n in range(N)]
B.sort()
# print(B)
b0 = statistics.median(B)
import math
b1 = math.floor(b0)
b2 = math.ceil(b0)

print(min(sum([abs(b-b1) for b in B]), sum([abs(b-b2) for b in B])))

