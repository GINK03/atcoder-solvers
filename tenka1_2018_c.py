
import collections
N = int(input())

A = [int(input()) for n in range(N)]
A.sort()
A = collections.deque(A)
B = collections.deque([])

tmp = A.copy()
while tmp:
    if tmp:
        B.append(tmp.pop())
    if tmp:
        B.appendleft(tmp.popleft())
    if tmp:
        B.append(tmp.popleft())
    if tmp:
        B.appendleft(tmp.pop())

tmp = A.copy()
C = collections.deque([])
while tmp:
    if tmp:
        C.append(tmp.popleft())
    if tmp:
        C.appendleft(tmp.pop())
    if tmp:
        C.append(tmp.pop())
    if tmp:
        C.appendleft(tmp.popleft())


ans0 = 0
for i in range(len(B)-1):
    ans0 += abs(B[i+1] - B[i])

ans1 = 0
for i in range(len(C)-1):
    ans1 += abs(C[i+1] - C[i])

# print(ans0, ans1)
print(max(ans0, ans1))

