

N,M=map(int,input().split())

AB = []
for _ in range(M):
    AB.append(list(map(int,input().split())))
AB.sort(key=lambda x:x[1])

tgt = -1

cnt = 0
for a, b in AB:
    if not(a < tgt <= b):
        tgt = b
        cnt += 1

print(cnt)

