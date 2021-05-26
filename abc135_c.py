
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))


ans = 0
for i,b in enumerate(B):
    first_beat = min(b, A[i])
    resid = b-first_beat
    second_beat = min(A[i+1], resid)
    A[i+1] -= second_beat
    ans += first_beat+second_beat
print(ans)
