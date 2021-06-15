
import statistics
import math
N=int(input())
*A,=map(int,input().split())
mean = statistics.mean(A)
can0, can1 = math.floor(mean), math.ceil(mean)

print(min([sum([(can-a)**2 for a in A]) for can in [can0, can1]]))



