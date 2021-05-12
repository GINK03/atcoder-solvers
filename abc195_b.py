A,B,W=map(int,input().split())
W*=1000

a = []
for n in range(1, 1000000+1):
    if A*n <= W <= B*n:
        a.append(n)

if not a:
    print("UNSATISFIABLE")
else:
    print(min(a), max(a))
