N, Q = map(int, input().split())

(*A,) = map(int, input().split())

shifts = 0
for _ in range(Q):
    T, x, y = map(int, input().split())
    if T == 1:
        x -= 1
        y -= 1
        A[(x + shifts) % N], A[(y + shifts) % N] = A[(y + shifts) % N], A[(x + shifts) % N]
    if T == 2:
        shifts = (shifts + N - 1) % N
    if T == 3:
        x -= 1
        print(A[(x + shifts) % N])
