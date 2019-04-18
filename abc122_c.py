N, Q = map(int, input().split())
So = input()
import re
S = So.replace('AC', '11')
S = re.sub('[A-Z]', '0', S)
Si = list(map(int, S))

'''
これがTLEするのはスライスしたあと、コピー、トリム、サムの
コストが高すぎるから
'''
for q in range(Q):
    s, e = map(int,input().split())
    si = Si[s-1:e]
    so = So[s-1:e]
    if So[s-1] == 'C':
        si.pop(0)
    if So[e-1] == 'A':
        si.pop()
    #print(si)
    print(sum(si)//2)

