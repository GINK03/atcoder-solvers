N, M = map(int, input().split())

# x:gcd
# M//x >= N:解はこの値より小さいか、
# x >= N:この値より大きくなるはず
ans = 1
x = 1
while x * x <= M:
    if M % x == 0:
        if x >= N:
            ans = max(ans, M//x)
        if M//x >= N:
            ans = max(ans, x)
    x += 1
print(ans)
