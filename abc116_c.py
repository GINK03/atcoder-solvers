
N=int(input())
H=list(map(int,input().split()))


st = 0
acc = 0
for h in H:
    if h > st:
        acc += abs(h-st)
        st += abs(h-st)
    st = min(h,st)
print(acc)

