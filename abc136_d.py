S=list(input())

Rbuff = []
Lbuff = []

#print(S)
B = [0]*len(S)

RLposi = None
for c in range(len(S)):
    if c == 0:
        Rbuff.append(c)
    else:
        if c != len(S)-1 and S[c] + S[c+1] == 'RL':
                B[c] += 1
        elif S[c-1] + S[c] == 'RL':
            RLposi = c
            B[c] += 1
            if Rbuff != []:
                for r in Rbuff:
                    if abs(c - r)%2 == 0:
                        B[c] += 1
                    else:
                        B[c-1] += 1
                Rbuff = []
        elif S[c] == 'R':
            Rbuff.append(c)
        elif S[c] == 'L':
            if RLposi is not None:
                if (c - RLposi)%2 == 0:
                    B[RLposi] += 1
                else:
                    B[RLposi-1] += 1
print(' '.join(map(str,B)))
