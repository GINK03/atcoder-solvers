from itertools import permutations
s1 = input()
s2 = input()
s3 = input()

all = set(s1 + s2 + s3)

if len(all) > 10:
    print("UNSOLVABLE")
    exit()


chidx = {ch: idx for idx, ch in enumerate(all)}
for pstable in permutations(range(10)):
    if pstable[chidx[s1[0]]] == 0 or pstable[chidx[s2[0]]] == 0 or pstable[chidx[s3[0]]] == 0:
        continue
    a1 = a2 = a3 = 0
    for i in range(len(s1)):
        a1 = a1 * 10 + pstable[chidx[s1[i]]]
    for i in range(len(s2)):
        a2 = a2 * 10 + pstable[chidx[s2[i]]]
    for i in range(len(s3)):
        a3 = a3 * 10 + pstable[chidx[s3[i]]]
    if a1 + a2 - a3 == 0:
        print(a1)
        print(a2)
        print(a3)
        exit()

print("UNSOLVABLE")
