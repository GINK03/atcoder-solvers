
N = int(input())


# w = (N∗h∗n)//(4∗h∗n − N∗n − N∗h)
def f(h,n):
    if h == n == 0 or (4*h*n-N*n-N*h) <= 0:
        return False
    return (N*h*n)%(4*h*n-N*n-N*h) == 0

for h in range(3501):
    for n in range(3501):
        if f(h,n):
            print(h,n, (N*h*n)//(4*h*n-N*n-N*h))
            exit()
