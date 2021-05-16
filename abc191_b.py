N,X=map(int,input().split())
A=list(map(int,input().split()))

print(*filter(lambda x:x!=X, A), sep=" ")
