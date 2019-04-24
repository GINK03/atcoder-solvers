N,M = map(int,input().split())

buff = []
for m in range(M):
    lst = list(map(int,input().split()))
    k=lst.pop(0)
    ss=[s-1 for s in lst]
    buff.append((k,ss))

ps=list(map(int, input().split()))

pats = []
for (k,ss),p in zip(buff, ps):
    pats.append((k,ss,p))


base = int('1'*N,2)

format = '{:0' + str(N) + 'b}'

cnt = 0
for i in range(base+1):
    check_tar = [int(x) for x in format.format(i)]
    ress = []
    for k,ss,p in pats:
        res = sum([check_tar[s] for s in ss])%2 == p
        ress.append(res)
    #print(ress, all(ress), format.format(i))
    if all(ress):
        cnt+=1

print(cnt)


