import collections
import heapq
Q = int(input())

L = collections.deque([])
H = []

is_heap = False
can_heap_num = 0
for q in range(Q):
    raw = input()
    if raw[0] == "1":
        x = int(raw.split()[1])
        L.append( (x, q) )
        heapq.heappush(H, (x, q) )
        if is_heap == False:
            can_heap_num += 1
    elif raw[0] == "2":
        if is_heap == False:
            print(L.popleft(), is_heap)
        else:
            print(heapq.heappop(H), is_heap, H)
            can_heap_num -= 1
        if can_heap_num == 0:
            is_heap == False
    else:
        # L.sort()
        is_heap = True
        pass
