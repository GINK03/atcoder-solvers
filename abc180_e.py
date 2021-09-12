


def main():
    inf = float("inf")
    
    N = int(input())
    XYZ = []
    for n in range(N):
        x,y,z = map(int,input().split())
        XYZ.append( (x, y, z) )

    edge = [[inf]*N for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, N):
            if i == j: continue
            xi,yi,zi = XYZ[i]
            xj,yj,zj = XYZ[j]
            edge[i][j] = abs(xi-xj) + abs(yi-yj) + max(0, zi-zj)
            edge[j][i]= abs(xi-xj) + abs(yi-yj) + max(0, -zi+zj)

    dp = [[inf] * N for _ in range(1<<N)]
    dp[0][0] = 0

    for mask in range(1<<N):
        for i in range(N):
            for j in range(N):
                if mask & 1 << i > 0 and i != j and edge[j][i] != inf:
                    dp[mask][i] = min(dp[mask][i], dp[mask^(1<<i)][j] + edge[j][i])

    print(dp[-1][0])

if __name__ == "__main__":
    main()
