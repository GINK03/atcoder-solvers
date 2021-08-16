
S, T = map(int, input().split())

cnt = 0
for a in range(S+1):
    for b in range(S+1):
        for c in range(S+1):
            if a + b + c <= S:
                if a * b * c <= T:
                    cnt += 1
print(cnt)
