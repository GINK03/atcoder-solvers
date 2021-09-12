import collections

cnt = collections.defaultdict(int)

N = int(input())

for n in range(N):
    s, t = input().split()
    cnt[(s, t)] += 1
    if cnt[(s, t)] >= 2:
        print("Yes")
        exit()
print("No")
