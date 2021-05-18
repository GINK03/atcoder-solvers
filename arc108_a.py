S,P=map(int,input().split())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

divs = make_divisors(P)

for div in divs:
    if P//div + div == S:
        print("Yes")
        exit()
print("No")
