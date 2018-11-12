N = input()
T,A = map(int, input().split())
Hs = [int(x) for x in input().split()]

cs = [(index,abs(A- (T-h*0.006))) for index,h in enumerate(Hs)]
cs = min(cs, key=lambda x:x[1])
print(cs[0]+1)

