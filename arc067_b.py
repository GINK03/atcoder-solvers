
N,A,B = map(int,input().split())
*X,=map(int,input().split())

acc = 0
for i in range(1, N):
    diff = X[i] - X[i-1]
    hirou_a = diff*A
    hirou_b = B
    acc += min(hirou_a, hirou_b)

print(acc)
