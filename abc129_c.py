
N, M = map(int,input().split())

ax = [1]*(N+1)
for m in range(M):
    ai = int(input()) - 1
    ax[ai+1] = None
# maybe ax[k] = ax[k-1] + ax[k-2]
#print(ax)

chunk_num = []
num = 0
for i in range(len(ax)):
    if ax[i] is not None:
        num += 1
    else:
        chunk_num.append(num)
        num = 0
chunk_num.append(num)

#print(chunk_num)
bu = {0:1, 1:1}
for i in range(1, max(chunk_num)):
    if bu.get(i) is None:
        bu[i] = bu[i-1] + bu[i-2]

rs = 1
for num in chunk_num:
    #print('l', num, bu[num-1])
    try:
        rs *= bu[num-1] 
    except:
        rs = 0
    rs %= 1000000007
print(rs%1000000007)
