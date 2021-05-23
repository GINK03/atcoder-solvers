
N=int(input())
A=[(v,i) for i,v in enumerate(map(int,input().split()), 1)]
A.sort()

print(*list(map(lambda x:x[1], A)))

