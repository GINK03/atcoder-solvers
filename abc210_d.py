

H,W,C=map(int,input().split())

G = [list(map(int,input().split())) for h in range(H)]

for h in range(H):
    for w in range(W):
        G[h][w] = (G[h][w], h, w)
def calc(h0, h1):
    c0, h0, w0 = h0
    c1, h1, w1 = h1
    return c0 + c1 + C*(abs(h0-h1) + abs(w0-w1))

def main():
    tmp = float("inf")
    for g in G:
        tmp0 = min(g)[0]
        tmp = min(tmp0, tmp)
    ini = []
    for h in range(H):
        for w in range(W):
            if G[h][w][0] == tmp:
                ini.append((h,w)) 
    ans = float("inf")
    for h, w in ini:
        t0 = G[h].copy()
        t0.sort()
        t1 = [G[h_][w] for h_ in range(H)]
        t1.sort()
        

        for h_ in range(1,H):
            ans = min(ans, calc(t1[0], t1[h_]))
        for w_ in range(1,W):
            ans = min(ans, calc(t0[0], t0[w_]))
    print(ans)

if __name__ == "__main__":
    main()
