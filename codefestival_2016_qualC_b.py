
K,T=map(int,input().split())
*A,=map(int,input().split())
A.sort()

max_a = A.pop()

print(max(max_a - sum(A) - 1, 0))
