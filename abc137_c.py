
from collections import Counter
N=int(input())

st = []
for n in range(N):
    s = ''.join(sorted(input()))
    st.append(s)

a = 0
for k, f in dict(Counter(st)).items():
    if f == 1:
        continue
    else:
       a += f*(f-1)/2

print(int(a))
