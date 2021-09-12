import itertools

MOD = 998244353
N = int(input())
S = input()
*S, = [(k, len(list(v))) for k, v in itertools.groupby(S)]
print(S)
ans = 0
def dfs(p, s, acc, l):
    global ans 
    if p == len(S):
        if s != set():
            ans += acc
            ans %= MOD
            # print(l, acc)
        return

    # none 
    dfs(p+1, s, acc, l)
    if S[p][0] not in s:
        s.add(S[p][0])
        l.append(S[p][0])
        dfs(p+1, s, (acc*S[p][1])%MOD, l)
        s.remove(S[p][0])
        l.pop()
    elif l[-1] == S[p][0]:
        l.append(S[p][0])
        dfs(p+1, s, (acc*S[p][1])%MOD, l)
        l.pop()

dfs(0, set(), 1, [])
print(ans)
