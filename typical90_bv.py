
N = int(input())
S = input()

ans = 0
for i in range(N):
    if S[i] == 'b':
        ans += (1<<i)
    elif S[i] == 'c':
        ans += 2*(1<<i)
print(ans)
