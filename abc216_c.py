
N = int(input())

ans = []
while True:
    if N%2 == 1:
        ans.append( ("A", N) )
        N -= 1
    else:
        ans.append( ("B", N))
        N //= 2
    if N == 0:
        break

#print(ans[::-1])
print(*[a[0] for a in ans[::-1]], sep="")

