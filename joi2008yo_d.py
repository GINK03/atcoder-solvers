M = int(input())
S = set()
for _ in range(M):
    x, y = map(int, input().split())
    S.add((x, y))

N = int(input())
T = set()
for _ in range(N):
    x, y = map(int, input().split())
    T.add((x, y))

for sx, sy in S:
    for tx, ty in T:
        dx=tx-sx
        dy=ty-sy
        # これだけずれていると仮定すると
        moved = set([(x-dx, y-dy) for x, y in T])
        # Tをシフトさせた結果がSの必要条件になっていればbreak
        if len(S) == len(S & moved):
            print(dx, dy)
            break
    else:
        continue
    break
