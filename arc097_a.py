import itertools

S=input()
K=int(input())

check = set()
for diff in itertools.count(1):
    # たかだか、答えはKの長さ以上にはならない
    if len(S) - diff < 0 or diff > K+1:
        break
    for i in range(len(S)-diff+1):
        k = i+diff
        check.add(S[i:k])
res = list(check)
res.sort()
print(res[K-1])
