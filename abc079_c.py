
S=list(input())
P=1<<3

for i in range(P):
    a=int(S[0])
    for j in range(0,2+1):
        if i&(1<<j) > 0:
            a += int(S[j+1])
        else:
            a -= int(S[j+1])
    if a == 7:
        bits = ['+' if b == '1' else '-' for b in reversed(list(f"{i:03b}"))]
        #print(S, bits, i)
        ans = ''
        for i in range(3):
            ans += str(S[i]) + bits[i]
        ans += str(S[-1]) + "=7"
        print(ans)
        exit()

