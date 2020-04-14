n = int(input())

state = int(input())
ax = [int(input()) for a in range(n-1)]

for now in ax:
    
    if now == state:
        print("stay")
    elif now > state:
        print('up %d'%(now-state))
    elif now < state:
        print('down %d'%(abs(now-state)))

    state = now
