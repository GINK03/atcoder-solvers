
N, K = map(int,input().split())

if K%2 == 1:
    num = N//K
    print(num**3)
else:
    num1 = N//(K//2)
    num2 = N//K
    print((num1-num2)**3 + num2**3)
