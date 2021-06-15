
N=int(input())

if N%2 == 1:
    print(0)
    exit()

acc = 0
b = 10
while True:
    if N < b:
        break
    acc += N//b
    b *= 5
print(acc)
