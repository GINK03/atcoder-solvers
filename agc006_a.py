N=int(input())
S=list(input())
T=list(input())

for i in range(2*N):
    s = S + [0]*i
    t = [0]*i + T

    flag = True
    for s0, t0 in zip(s, t):
        if s0 == 0 or t0 == 0:
            continue
        if s0 != t0:
            flag = False
    # print(s)
    # print(t)
    if flag:
        break

char = ''
for s0, t0 in zip(s, t):
    if s0 == 0 or t0 == 0:
        char += s0 if s0 else t0
    else:
        char += s0
print(len(char))
