import collections
import math
N=int(input())
A=list(map(int,input().split()))

dic = dict()
total = 0
for k, v in collections.Counter(A).items():
    total += math.comb(v,2)
    dic[k] = math.comb(v,2) - math.comb(v-1,2)


for a in A:
    print(total-dic[a])


