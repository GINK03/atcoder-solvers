k, n = map(int,input().split())
xs = list(map(int,input().split()))
xs = xs + [x+k for x in xs]

ans = float('inf')
for i in range(n):
    delta = xs[i+n-1] - xs[i]
    ans = min(delta, ans)

print(ans)
