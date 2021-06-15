

from collections import Counter
N=int(input())
A=list(map(int, input().split()))
C=Counter(A)
if C[0]==N:
    print("Yes")
elif N%3==0 and C[0]==N//3 and len(C)==2:
    print("Yes")
elif len(C)==3:
    tmp=[]
    for key, val in C.items():
        tmp.append(key)
        if val==N//3:
            continue
        else:
            print("No")
            exit()
    if tmp[0]^tmp[1]==tmp[2]:
        print("Yes")
    else:
        print("No")
else:
    print("No")
