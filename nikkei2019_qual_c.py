
# greedyアルゴリズムの一つのdifferent strokeが適応例
# Aがえる利益 a - (-b) = a + b -> Bが失う利益と得るの差分
# Bがえる利益 b - (-a) = b + a -> Aが失う利益と得るの差分

N = int(input())

A = []
for _ in range(N):
    a, b = map(int,input().split())
    dif = a + b
    A.append( (dif, a, b) )
A.sort()
A = A[::-1]

a_cum, b_cum = 0, 0
for i, (dif, a, b) in enumerate(A):
    if i%2 == 0:
        a_cum += a
    else:
        b_cum += b
print(a_cum - b_cum)

