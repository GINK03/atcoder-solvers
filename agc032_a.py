
N=int(input())
*B,=map(int,input().split())


A = []
while True:
    flg = True
    if not B:
        break
    for i in range(len(B)-1, -1, -1):
        if B[i] == i+1:
            a = B.pop(i)
            A.append(a)
            flg = False
            break
    if flg:
        "illigal"
        print(-1)
        exit()

print(*A[::-1], sep="\n")
