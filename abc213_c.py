
H, W, N = map(int, input().split())

AB = []
for n in range(N):
    AB.append(list(map(int,input().split())))
A = [a for a,b in AB]
B = [b for a,b in AB]

ma = {a:i for i, a in enumerate(sorted(set(A)), 1)}
mb = {b:i for i, b in enumerate(sorted(set(B)), 1)}

for a, b in AB:
    print(ma[a], mb[b])
