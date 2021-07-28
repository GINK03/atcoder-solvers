

N = int(input())
A = [int(input()) for n in range(N)]

if all(a%2 == 0 for a in A):
    print("second")
else:
    print("first")


