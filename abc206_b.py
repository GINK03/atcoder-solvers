

N = int(input())

c = 0
while True:
    c += 1
    if c*(c+1)//2 >= N:
        print(c)
        break

