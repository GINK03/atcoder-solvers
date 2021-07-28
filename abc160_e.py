
X,Y,A,B,C = map(int,input().split())

*AR, = map(int,input().split())
*BR, = map(int,input().split())
*CR, = map(int,input().split())

AR.sort(); BR.sort(); CR.sort()
e = sorted(AR[-X:] + BR[-Y:] + CR)
print(sum(e[-(X+Y):]))

