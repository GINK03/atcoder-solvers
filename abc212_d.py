import heapq

Q = int(input())
que = []
heapq.heapify(que)
acc = 0
for q in range(Q):
    *raw, = map(int, input().split())
    if raw[0] == 1:
        x = raw[1]
        heapq.heappush(que, x - acc) 
    if raw[0] == 2:
        acc += raw[1]
    if raw[0] == 3:
        print(heapq.heappop(que) + acc)
    # print(que)
