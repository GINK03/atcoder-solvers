import copy
N = int(input())

A, B, C, D, E = [int(input()) for i in range(5)]
Xs = [N, 0, 0, 0, 0, 0]
Fs = [A, B, C, D, E]
Fmin = min(Fs)
c = 0
while True:
    #print(Xs)
    nXs = copy.copy(Xs)
    for i in range(len(Fs)):
        if Xs[i] - Fs[i] > 0:
            nXs[i] -= Fs[i]
            nXs[i+1] += Fs[i]
        else:
            nXs[i] -= Xs[i]
            nXs[i+1] += Xs[i]
        #print(nXs)
    Xs = nXs
    c+=1
    if max(Xs[1:5]) == Fmin:
        c+=Xs[0]//Fmin
        Xs[0]%=Fmin
    if sum(Xs[0:5]) == 0:
        break
    
print(c)
