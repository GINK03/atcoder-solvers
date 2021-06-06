
import re
N=int(input())
S=input()
K=int(input())

a = S[K-1]

print(re.sub(f"[^{a}]", "*", S))
