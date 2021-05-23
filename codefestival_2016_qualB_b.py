
N,A,B=map(int,input().split())
S=input()

cnt=0
bnum=0
for s in S:
    if s == 'c':
        print("No")
        continue
    if s == 'a':
        if cnt < A+B:
            cnt += 1
            print("Yes")
        else:
            print("No")
    if s == 'b':
        if bnum < B and cnt < A+B:
            bnum += 1
            cnt += 1
            print("Yes")
        else:
            print("No")
    #print(cnt, bnum)
