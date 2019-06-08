N=int(input())
xs =[]
for n in range(N):
    xy=list(map(int,input().split()))
    xs.append(xy)

key_freq = {}
for n in range(N):
    for k in range(n+1,N):
        nx, kx = xs[n], xs[k]
        key = (nx[0]-kx[0], nx[1]-kx[1])
        if key_freq.get(key) is None:
            key_freq[key] = 0
        key_freq[key] += 1

try:
    last_key_freq = sorted([(key,freq) for key, freq in key_freq.items()],key=lambda x:x[1])[-1]
except:
    print(1)
    exit()

max_freq = last_key_freq[1]
cs = []
for key, freq in key_freq.items():
    if max_freq != freq:
        continue
    #print(key)
    x_n ={}
    for x in xs:
        x_n[tuple(x)] = (x[0] + key[0],x[1]+key[1])
    c=0
    for x, n in x_n.items():
        if n in x_n:
            c+=0
        else:
            c+=1
    #print(c, key)
    cs.append(c)
print(min(cs))
