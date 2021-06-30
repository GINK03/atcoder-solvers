
S=list(input())
R=S[::-1]

cnt = dict()
c = 0
for i in range(0, len(S)):
    c += int(R[i])*pow(10, i, 2019)
    c %= 2019
    cnt[c] = cnt.get(c,0) + 1

# cnt[0] = cnt.get(0,0) + 1

ans = 0
for c, v in cnt.items():
    ans += v * (v-1) // 2
print(ans + cnt.get(0,0))




