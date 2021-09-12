
B = "abcdefghijklmnopqrstuvwxyz"
B = {i:b for i,b in enumerate(B)}

*A, = map(int, input().split())

ans = [B[a-1] for a in A]
print(*ans, sep="")
