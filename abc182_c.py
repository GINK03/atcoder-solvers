
S=input()
L=len(S)

ans = float("inf")
for i in range(1<<L):
    tmp = ''
    for j in reversed(range(L)):
        if i&(1<<j) > 0:
            tmp += S[j]
    if tmp == "":
        continue
    num = int(tmp)
    if num%3 == 0:
        ans = min(ans, L-len(tmp))
if ans == float('inf'):
    print(-1)
else:
    print(ans)
