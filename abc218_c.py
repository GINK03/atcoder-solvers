
import numpy as np

N = int(input())

def scan():
    base = [[0]*N for n in range(N)]
    ti = 0
    for i in range(N):
        for j, c in enumerate(input()):
            if c == "#":
                base[i][j] = 1
    base = np.array(base)
    del_label = []
    for i in range(N):
        if base[i].sum() == 0:
            del_label.append(i)
        else:
            break
    for i in range(N)[::-1]:
        if base[i].sum() == 0:
            del_label.append(i)
        else:
            break
    base = np.delete(base, del_label, 0) 
    del_label2 = []
    for i in range(N):
        if base[:, i].sum() == 0:
            del_label2.append(i)
        else:
            break
    for i in range(N)[::-1]:
        if base[:, i].sum() == 0:
            del_label2.append(i)
        else:
            break
    base = np.delete(base, del_label2, 1) 
    return base

S = scan()
T = scan()

s = np.array(S)
t = np.array(T)
    
def eval(s, t):
    if s.flatten().tolist() == t.flatten().tolist():
        return True
    else:
        return False

if eval(s,t) or\
    eval(np.rot90(s), t) or \
    eval(np.rot90(np.rot90(s)), t) or\
    eval(np.rot90(np.rot90(np.rot90(s))), t):

    print("Yes")
else:
    print("No")
