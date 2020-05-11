n,k=map(int,input().split())

aa=list(map(int,input().split()))

fumi = set([0])
start = None
end = None
aab = [0]
for i in range(10**18):
    next = aa[aab[-1]] - 1
    if next in fumi:
        if start is None:
            start = i
            fumi = set()
        else:
            end = i
            break

    aab.append(next)
    fumi.add(next)
    if i+1 == k:
        print(next+1)
        exit(0)

random_first = len(aab) - 2*(end - start)
#print(aab, start, end, aab[start+1:end+1], aab[:random_first])

first = aab[:random_first]
one_cicle = aab[start+1:end+1]
if k <= len(first):
    print(first[k]+1)
else:
    k = k-len(first)
    print(one_cicle[k%len(one_cicle)]+1)


