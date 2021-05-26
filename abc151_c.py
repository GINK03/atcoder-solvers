import collections
st = collections.defaultdict(int)
cnt = collections.defaultdict(int)
N,M=map(int,input().split())

for _ in range(M):
    p, s = input().split()
    p=int(p)
    if s == 'AC':
        st[p] = 1
        continue
    if st[p] == 0 and s == 'WA':
        cnt[p] += 1

for p, s in st.items():
    if s == 0:
        cnt[p] = 0

print(list(st.values()).count(1), sum(cnt.values()))
