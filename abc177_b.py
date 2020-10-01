S=list(input())
T=list(input())

T_size = len(T)

def match_num(x):
    return T_size - sum([1 for a,t in zip(x, T) if a==t])

b=[]
for i in range(len(S)-T_size+1):
    b.append(match_num(S[i:i+T_size]))

print(min(b))
