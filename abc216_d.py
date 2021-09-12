import heapq
import collections
N, M = map(int, input().split())

memo = collections.defaultdict(list)
tmp = []
for m in range(M):
    k = int(input())
    *a, = map(int, input().split())
    tmp.append(collections.deque(a))
    memo[a[0]-1].append(m)

removes = collections.deque()
for k, v in memo.items():
    if len(v) == 2:
        removes.append(k)

while removes:
    num = removes.popleft()
    for m in memo[num]:
        tmp[m].popleft()
        if tmp[m]:
            head = tmp[m][0]-1
            memo[head].append(m)
            if len(memo[head]) == 2:
                removes.append(head)

for m in range(M):
    if tmp[m]:
        print("No")
        exit()
print("Yes")
