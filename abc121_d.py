

A, B = map(int, input().split())

a = A - 1
b = B

def calc(x):
    if x%2 == 0:
        return calc(x+1) ^ (x+1)
    else:
        if ((x+1)//2)%2 == 0:
            return 0
        else:
            return 1

print(calc(b) ^ calc(a))
