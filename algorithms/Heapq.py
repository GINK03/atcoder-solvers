from heapq import heappop, heappush

h = []
heappush(h, (5, 'a'))
heappush(h, (7, 'b'))
heappush(h, (1, 'c'))
heappush(h, (4, 'd'))

print(heappop(h))
