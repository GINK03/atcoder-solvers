
S = input()

cur, max_ = 0, 0
for c in S:
    if c in {'A', 'C', 'G', 'T'}:
        cur += 1
    else:
        max_ = max(cur, max_)
        cur = 0
max_ = max(cur, max_)
print(max_)


