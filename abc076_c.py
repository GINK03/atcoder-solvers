
S=input()
T=input()

cands = []
for i in range(len(S) - len(T)+1):
    is_can = True
    for j in range(len(T)):
        if not(S[i+j] == "?" or T[j] == S[i+j]):
            is_can = False
            break
    if is_can:
        cands.append( (S[:i] + T + S[i+len(T):]).replace("?", "a") )

if cands:
    cands.sort()
    print(cands[0])
else:
    print("UNRESTORABLE")

