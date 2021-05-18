
T=int(input())
N=int(input())
A=list(map(int,input().split()))
M=int(input())
B=list(map(int,input().split()))


res = []
for j in range(len(B)):
    b = B[j]
    is_match = []
    for i in range(len(A)):
        a = A[i]
        if 0 <= b-a <= T:
            A.pop(i)
            is_match.append(True)
            break
        is_match.append(False)
    res.append(any(is_match) if is_match != [] else False)
#print(res) 
if all(res) is False:
    print("no")
else:
    print("yes")
