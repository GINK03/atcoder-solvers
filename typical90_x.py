
N,K=map(int,input().split())
*A,=map(int,input().split())
*B,=map(int,input().split())

s = sum([abs(a-b) for a,b in zip(A,B)])
if s <= K:
    if (K-s)%2 == 0:
        print("Yes")
        exit()
print("No")
