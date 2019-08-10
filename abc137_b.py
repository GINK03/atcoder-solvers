
K,X = map(int,input().split())

mini = X-K
for m in range(X-K+1, X+K):
    print(m, end=" ")
print()
