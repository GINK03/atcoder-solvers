
As = []
for i in range(5):
    x = int(input())
    if x%10 != 0:
        time_b = (x//10 + 1)*10
    else:
        time_b = (x//10 )*10

    amari  = x%10
    if amari == 0:
        amari = float('inf')
    As.append((amari, x, time_b))

As = sorted(As, key=lambda x:x[0])
#print(As)
#print([x[2] for x in As[1:] if x[2] != 0])
sumed = sum([x[2] for x in As[1:] if x[2] != 0 ])

print(sumed + As[0][1])
