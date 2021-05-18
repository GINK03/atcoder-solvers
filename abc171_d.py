
N=int(input())
A=list(map(int,input().split()))
Q=int(input())
import collections
dic = dict(collections.Counter(A)) 
total = sum([k*v for k,v in dic.items()])

for _ in range(Q):
    b,c=map(int,input().split())
    if b not in dic:
        dic[b] = 0
    if c not in dic:
        dic[c] = 0
    total += dic[b] * c - dic[b] * b
    dic[c] += dic[b]
    dic[b] = 0
    print(total)
