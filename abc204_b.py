
N=int(input())
*A,=map(int,input().split())

acc = 0
for a in A:
    if a > 10:
        acc += a - 10
print(acc)

