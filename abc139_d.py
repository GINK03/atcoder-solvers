
N=int(input())


"""
*A,=range(1,N+1)
acc = 0
for a, b in zip(A, A[1:] + [A[0]]):
    # print(a, b)
    m = a%b
    acc += m
print(acc)
"""

n=N-1
a = n*(n+1)//2
print(a)

