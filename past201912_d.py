
n = int(input())

ax = [int(input()) for i in range(n)]

n_c = {}
for i in range(1, n+1):
    n_c[i] = 0
for a in ax:
    n_c[a] += 1

correct = all([c==1 for n,c in n_c.items()])

if correct:
    print("Correct")
else:
    max_ = [n for n,c in n_c.items() if c == 2][0]
    min_ = [n for n,c in n_c.items() if c == 0][0]
    print(max_, min_)


