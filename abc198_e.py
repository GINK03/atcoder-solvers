from collections import defaultdict
import collections
N = int(input())
C = [0] + list(map(int, input().split()))


color = defaultdict(int)
ans = []

graph = defaultdict(list)
for n in range(N-1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

# Driver Code
visited = set()  # Set to keep track of visited nodes.
stack = collections.deque([1])
while stack:
    loc = stack.pop()
    if loc in visited:
        color[C[loc]] -= 1
        continue
    else:
        if color[C[loc]] == 0:
            ans.append(loc)
        visited.add(loc)
        color[C[loc]] += 1
        stack.append(loc)
        for l in graph[loc]:
            if l not in visited:
                stack.append(l)
ans.sort()
print(*ans, sep="\n")
