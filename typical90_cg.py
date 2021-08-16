
K = int(input())

# 素因数分解
divs = []
for i in range(1, int(K**0.5) + 1):
    if K%i == 0:
        divs.append(i)

# ２変数を探索
cnt = 0
for i in range(len(divs)):
    for j in range(i, len(divs)):
        a, b = divs[i], divs[j]
        if K%(a*b) == 0:
            c = K//(a*b)
            if a <= b <= c:
                # print(a, b, c)
                cnt += 1
print(cnt)

