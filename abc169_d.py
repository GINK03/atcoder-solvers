
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

n = int(input())
if n == 1:
    print(0)
    exit()
pfs = factorization(n)

cs = 0
for p, f in pfs:
    c = 0
    for i in range(10**12):
        f -= i
        if f < 0:
            c = i-1
            break
    # print(p,c)
    cs += c
print(cs)

