

N = int(input())
S = input()

wn = S.count(".")
bn = 0

ans = wn
for n in range(N):
    if S[n] == "#":
        bn += 1
    else:
        wn -= 1
    ans = min(ans, bn+wn) 
print(ans)

