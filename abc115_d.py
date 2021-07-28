
N, X = map(int, input().split())

a = [1]
p = [1]
for i in range(N):
    p.append(p[-1]*2 + 1)
    a.append(a[-1]*2 + 3)

def cal(n,x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + a[n-1]:
        return cal(n-1, x-1)
    else:
        return p[n-1] + 1 + cal(n-1, x-2-a[n-1])
print(cal(N,X))
