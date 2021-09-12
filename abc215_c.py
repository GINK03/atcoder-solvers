
S, K = input().split()
K = int(K)
import itertools

*b, = itertools.permutations(S, len(S))
b = list(set(b))
b.sort()
print("".join(b[K-1]))
#print(b)
