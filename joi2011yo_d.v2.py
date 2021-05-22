import collections
N=int(input())
A=list(map(int,input().split()))
que = collections.deque([(0,A[0])])
cnt = 0
while que:
    i,v = que.pop()
    if i == len(A)-2:
        if v == A[-1]:
            cnt += 1
        continue

    if 0 <= v+A[i+1] <= 20:
        que.append((i+1,v+A[i+1]))
    if 0 <= v-A[i+1] <= 20:
        que.append((i+1,v-A[i+1]))
print(cnt)
     
    
