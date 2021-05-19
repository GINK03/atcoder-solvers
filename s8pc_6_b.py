
N=int(input())
A,B=[],[]
for _ in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)


ans = float('inf')
for a in A:
    for b in B:
        s = a
        e = b
        dist = 0
        for a_, b_ in zip(A,B):
            dist += abs(s-a_) + abs(b_-a_) + abs(e-b_)
        ans = min(ans, dist)
print(ans)

