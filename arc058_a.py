import itertools

N,K=map(int,input().split())
*D,=map(int,input().split())
D = set(D)

for cnt in itertools.count(N):
    if len(set(map(int, str(cnt))) & D) >= 1:
        continue
    else:
        print(cnt)
        break
