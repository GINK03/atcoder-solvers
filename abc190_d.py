
N=int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

# 奇数の約数が解の候補になる
# 対象性があるので二倍する

divs = make_divisors(N)

cnt = 0
for div in divs:
    if div%2 != 0:
        cnt += 2
print(cnt)
