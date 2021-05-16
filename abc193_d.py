K = int(input())
S = input()[:4]
T = input()[:4]

cnt = [K] * 10
for c in S:
    cnt[int(c)] -= 1
for c in T:
    cnt[int(c)] -= 1


def score(S):
    cnt = [0] * 10
    for c in S:
        cnt[int(c)] += 1
    ans = 0
    for i in range(1, 10):
        ans += i * 10 ** cnt[i]
    return ans


ans = 0
for i in range(1, 10):
    if cnt[i] == 0:
        continue
    for j in range(1, 10):
        if i == j or cnt[j] == 0:
            continue
        if score(S + str(i)) > score(T + str(j)):
            ans += cnt[i] * cnt[j]

for i in range(1, 10):
    if cnt[i] < 2:
        continue
    if score(S + str(i)) > score(T + str(i)):
        ans += cnt[i] * (cnt[i] - 1)

N = 9 * K - 8
print(ans / N / (N - 1))
