

A = ["H", "2B", "3B", "HR"]
A.sort()

B = [input() for i in range(4)]
B.sort()

if A == B:
    print("Yes")
else:
    print("No")
