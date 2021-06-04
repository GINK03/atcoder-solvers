
def lcs(s1, s2):
    n1, n2 = len(s1), len(s2)
    M = [[0]*(n2+1) for _ in range(n1+1)]
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                M[i][j] = M[i-1][j-1] + 1
            if s1[i-1] != s2[j-1]:
                M[i][j] = max(M[i][j-1], M[i-1][j])
    return (int(M[n1][n2]), M)

N = int(input())
S = input()

ans = 0
for i in range(0,N):
    a, _ = lcs(S[:i], S[i:])
    ans = max(a, ans)
print(N-ans*2)
