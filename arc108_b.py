import collections

N=int(input())
S=input()
right = collections.deque(S)
left = collections.deque([None, None, None])

while right:
    left.append(right.popleft())

    if left[-3] == "f" and left[-2] == "o" and left[-1] == "x":
        for i in range(3):
            left.pop()

print(len([x for x in  left if x]))

