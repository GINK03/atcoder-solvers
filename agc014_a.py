import itertools
x=list(map(int,input().split()))


prev = None
for cnt in itertools.count(0):
    if all(list(map(lambda x:x%2==0, x))):
        t0 = [a//2 for a in x]
        x = [ t0[1]+t0[2], t0[0]+t0[2], t0[1]+t0[0] ] 
        if prev == x:
            print(-1)
            exit()
        prev = x
    else:
        print(cnt)
        break
        


