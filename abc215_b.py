
N = int(input())

b = 2
for i in range(1, 10**5):
    if b > N:
        print(i-1)
        exit()
    b *= 2

