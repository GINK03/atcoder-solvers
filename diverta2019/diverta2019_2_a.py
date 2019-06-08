n,k=map(int,input().split())
xs=[1]*k
xs[0]+=n-k
print(max(xs)-min(xs))

