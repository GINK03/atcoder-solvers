import itertools
N=int(input())
ax=list(map(int,input().split()))
acc0=list(itertools.accumulate(ax))
acc1=list(reversed(list(itertools.accumulate(reversed(ax)))))

#print(acc0)
#print(acc1)

ans = float('inf')
for i in range(N-1):
    ans = min(ans, abs(acc0[i] - acc1[i+1]))
print(ans)


