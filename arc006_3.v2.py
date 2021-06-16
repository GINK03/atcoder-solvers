

N = int(input())

G = []

for n in range(N):
    w = int(input())
    for g in G:
        if g[-1] >= w:
            g.append(w)
            break
    else:
        G.append( [w] )

print(len(G))

