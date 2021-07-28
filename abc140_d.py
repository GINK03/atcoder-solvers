import itertools
N, K = map(int,input().split())
S = input()
*GRP, = itertools.groupby(S)

print(N - max(len(GRP)-2*K, 1))
