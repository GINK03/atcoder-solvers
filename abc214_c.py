import heapq
N = int(input())
*S, = map(int, input().split())
*T, = map(int, input().split())

que = []

movs = [None] * N
for i in range(len(S)):
    e = (S[i], "mov", i, S[i])
    movs[i] = e
    #que.append(e)

for i in range(len(T)):
    e = (T[i], "new", i, 0)
    que.append(e)

heapq.heapify(que)

tbl = [0] * N
new = [0] * N
cnt = 0
acc = 0
while que:
    e = heapq.heappop(que)
    val, mode, idx, step = e
    acc += step
    if mode == "mov":
        if tbl[idx] == 1:
            if new[(idx+1)%N] == 0:
                new[(idx+1)%N] = val
                cnt += 1
                _, _mode, _idx, _step = movs[(idx+1)%N]
                heapq.heappush(que, (val + _step, _mode, _idx, _step) )
            tbl[(idx+1)%N] = tbl[idx]
            tbl[idx] = 0
        # heapq.heappush(que, (val + step, mode, idx, step) )
    elif mode == "new":
        if new[idx] == 0:
            new[idx] = val
            cnt += 1
            _, _mode, _idx, _step = movs[idx]
            heapq.heappush(que, (val + _step, _mode, _idx, _step) )
        tbl[idx] = 1
    else:
        raise Exception(mode)
    # print(new, e, que)
    if cnt == N:
        break

print(*new, sep="\n")
    
