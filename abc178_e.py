n=int(input())

z, w = [], []
for _ in range(n):
    x1, x2=map(int,input().split())
    z.append(abs(x1+x2))
    w.append(abs(x1-x2))


print(max(max(z)-min(z), max(w)-min(w)))
