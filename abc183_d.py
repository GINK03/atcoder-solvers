
N, W = map(int, input().split())

B=[0] * (2*(10**5) + 2)

for n in range(N):
    S, T, P = map(int, input().split())
    B[S] += P
    B[T] -= P

#print(B[:12])
buff = 0
for b in B:
    buff += b
    if buff > W:
        print("No")
        exit()
print("Yes")
