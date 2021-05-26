
a,b=map(int,input().split())

if a <= 0 <= b:
    print("Zero")
elif 1 <= a:
    print("Positive")
elif b < 0:
    if (b-a)%2 == 0:
        print("Negative")
    else:
        print("Positive")
