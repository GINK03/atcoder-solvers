
N = int(input())
*A, = map(int, input().split())
*A, = [(a,i) for i, a in enumerate(A,1)]
A.sort()
print(A[-2][1])
