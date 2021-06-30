
N=int(input())
*A,=map(int,input().split())
*B,=map(int,input().split())

needs = [b-a for b,a in zip(B,A) if b-a > 0]
need = sum([b-a for b,a in zip(B,A) if b-a > 0])
over = [a-b for b,a in zip(B,A) if a-b > 0]
over.sort()


cnt = 0
acc = 0
while acc < need:
    if over == []:
        print(-1)
        exit()
    max_ = over.pop()
    acc += max_
    cnt += 1

print(len(needs) + cnt)
